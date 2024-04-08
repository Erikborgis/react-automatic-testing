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

    for file, path in tsx_files_and_paths:
        react_component_text = file_reader.read_file(path)
        file_name = os.path.splitext(file)[0]
        if react_component_text:
            test_content = write_to_gpt.call_openai_api(react_component_text, path)
            
            # Regenerates unit tests until the tests pass. Max 10 tries.
            number_of_tries = 1
            pass_status = False
            while(True and number_of_tries < 6):
                generate_test_file.generate_test_file(test_content, file_name)
                
                test_status, test_message  = run_test.run_test(file_name)
                
                if(test_status):
                    pass_status = True
                    break
                else:
                    # Reruns the test generation
                    test_content = write_to_gpt.call_openai_api(react_component_text, path)
                    number_of_tries += 1
            
            test_generation_statistics.append((file_name, number_of_tries, pass_status))
    
    # run_test.run_eslint()
    coverage = code_coverage.check_coverage_all_tests()
    analyze_tests.generate_csv_files(test_generation_statistics, coverage)
