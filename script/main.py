import file_reader
import write_to_gpt
import generate_test_file
import run_test
import find_react_components
import code_coverage
import analyze_tests
import os

if __name__ == "__main__":
    
    cwd = os.getcwd()

    # Searches all folders in root folder for react components. Tuple with both filename and realtive path of the react components.
    tsx_files_and_paths = find_react_components.search_files(cwd, ".tsx")

    test_generation_statistics = []

    stop_temperature = 0.5 # Maximum temperature, max temp = 2 For coding openAi recommends <= 0.5
    start_temperature = 0.1 # What temperature it should start on minimum = 0
    steps_temperature = 5 # How many steps it should take betwen stop and start. This is how many test files will be generated. This should be a whole number.

    for file, path in tsx_files_and_paths:
        react_component_text = file_reader.read_file(path)
        file_name = os.path.splitext(file)[0]
        if react_component_text:

            temps_ran = 0
            while(True and temps_ran < steps_temperature):

                temperature = stop_temperature / (temps_ran + 1)
                test_content = write_to_gpt.call_openai_api(react_component_text, path, temperature)
                
                if (temps_ran == 0):
                    temp_file_name = file_name
                else:
                    temp_file_name = file_name + f"{temps_ran}"

                # Regenerates unit tests until the tests pass. Max 10 tries.
                number_of_tries = 0
                pass_status = False
                while(True and number_of_tries < 5):
                    generate_test_file.generate_test_file(test_content, temp_file_name)
                    
                    test_status, test_message  = run_test.run_test(temp_file_name)
                    
                    if(test_status):
                        pass_status = True
                        break
                    else:
                        # Reruns the test generation
                        test_content = write_to_gpt.call_openai_api(react_component_text, path)
                        number_of_tries += 1
                
                test_generation_statistics.append((file_name, number_of_tries, pass_status))

                temps_ran += 1
    coverage = code_coverage.check_coverage_all_tests()
    analyze_tests.generate_csv_files(test_generation_statistics, coverage)
