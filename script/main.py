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
    steps_temperature = 2 # How many steps it should take betwen stop and start. This is how many test files will be generated. This should be a whole number.

    for file, path in tsx_files_and_paths:
        react_component_text = file_reader.read_file(path)
        file_name = os.path.splitext(file)[0]
        if react_component_text:
            analyze_tests.generate_csv_file(file_name)
            temperature_runs = 0
            while(True and temperature_runs < steps_temperature):

                temperature = stop_temperature / (temperature_runs + 1)
                test_content = write_to_gpt.call_openai_api(react_component_text, path, temperature)
                
                if (temperature_runs == 0):
                    temperature_file_name = file_name
                else:
                    temperature_file_name = file_name + f"{temperature_runs}"

                # Regenerates unit tests until the tests pass. Max 10 tries.
                number_of_tries = 1
                pass_status = False
                max_number_tries = 6
                while(True and number_of_tries < max_number_tries):
                    generate_test_file.generate_test_file(test_content, temperature_file_name)
                    
                    test_status, test_message  = run_test.run_test(temperature_file_name)
                    
                    if(test_status):
                        pass_status = True
                        break
                    else:
                        # Reruns the test generation
                        test_content = write_to_gpt.call_openai_api(react_component_text, path, temperature)
                        number_of_tries += 1
                        
                test_generation_statistics = [number_of_tries, pass_status, temperature]

                coverage = code_coverage.check_coverage_specific_test(f"tests/{temperature_file_name}.test.js")
                print(coverage)
                temperature_runs += 1
                analyze_tests.append_to_csv_files(file_name, test_generation_statistics, coverage, temperature_file_name) 
