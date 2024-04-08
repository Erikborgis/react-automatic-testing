import os
import write_to_gpt
import file_operations
import test_handler
import find_react_components
import code_coverage
import csv_operations

def main():
    cwd = os.getcwd()

    # Searches all folders in root folder for react components. Tuple with both filename and realtive path of the react components.
    tsx_files_and_paths = find_react_components.search_files(cwd, ".tsx")

    stop_temperature = 0.5  # Maximum temperature, max temp = 2 For coding openAi recommends <= 0.5
    steps_temperature = 2  # How many steps it should take between stop and start. This is how many test files will be generated per react component. This should be a whole number.

    for file_name, path in tsx_files_and_paths:
        react_component_text = file_operations.read_file(path)
        if react_component_text:
            csv_operations.generate_csv_file(file_name)
            for temperature_iteration in range(steps_temperature):
                temperature = stop_temperature / (temperature_iteration + 1)
                
                # Generate unit test with openai api.
                test_content = write_to_gpt.call_openai_api(react_component_text, path, temperature)
                
                test_file_name = f"{file_name}.test.js" if temperature_iteration == 0 else f"{file_name}{temperature_iteration}.test.js"

                # Regenerates unit tests until the tests pass. Max 5 tries.
                pass_status = False
                for number_of_tries in range(1, 6):
                    
                    # Generate test file and check if the test runs correctly
                    file_operations.create_test_file(test_content, test_file_name)
                    test_status = test_handler.run_test(test_file_name)

                    if test_status:
                        pass_status = True
                        break
                    else:
                        # Regenerate the test on failure
                        test_content = write_to_gpt.call_openai_api(react_component_text, path, temperature)
                
                # Check the code coverage on the react component the test is responsible for.
                coverage = code_coverage.check_coverage_specific_test(test_file_name)

                # Add parameters to create statistics file.
                csv_operations.append_to_csv_files(file_name, number_of_tries, pass_status, temperature, coverage, test_file_name) 

if __name__ == "__main__":
    main()
