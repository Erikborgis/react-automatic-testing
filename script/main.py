import os
import write_to_gpt
import file_operations
import test_handler
import find_react_components
import code_coverage
import csv_operations
import gpt_prompts
import os
import threading

semaphore = threading.Semaphore(15)

def process_react_component(file_name, path):

    try:
        max_number_of_tries = 2 # Specify how many retries the test generation should make if test fails. Must be more than one.
        temperature = [0.4]
        reruns = 2 # Specifies how many times a certain file should be rerun

        react_component_text = file_operations.read_file(path)
            
        if react_component_text:
            csv_operations.generate_csv_file(file_name)
            for rerun in range(reruns):
                for temp in temperature:                   
                    test_file_name = f"{file_name}_{rerun}_{temp}.test.js"
                    
                    gpt_message = gpt_prompts.first_prompt(react_component_text, path)
                    test_content = write_to_gpt.call_openai_api(gpt_message, temp)

                    # Generate test file and check if the test runs correctly
                    file_operations.create_test_file(test_content, test_file_name)
                    test_status, test_log = test_handler.run_test(test_file_name)

                    print(test_log)

                    # Regenerates unit tests until the tests pass. Max 5 tries.
                    if test_status:
                        number_of_tries = 1
                    else:
                        created_test_file = react_component_text = file_operations.read_file(f"./tests/{test_file_name}")
                        test_files = [created_test_file]
                        test_errors = [test_log]
                        for number_of_tries in range(2, max_number_of_tries + 1):
                            
                            assistant_prompts = gpt_prompts.create_assistant_prompts(test_files, test_errors)

                            gpt_message = gpt_prompts.retry_prompt(react_component_text, path, assistant_prompts)

                            test_content = write_to_gpt.regenerate_test(gpt_message, temp)

                            # Generate test file and check if the test runs correctly
                            file_operations.create_test_file(test_content, test_file_name)
                            test_status, test_log = test_handler.run_test(test_file_name)
                            if test_status:
                                break
                            else:
                                created_test_file = react_component_text = file_operations.read_file(f"tests/{test_file_name}")
                                test_files.append(created_test_file)
                                test_errors.append(test_log)

                    # Check the code coverage on the react component the test is responsible for.
                    coverage = code_coverage.check_coverage_specific_test(test_file_name)
                    # Add parameters to create statistics file.
                    csv_operations.append_to_csv_files(file_name, number_of_tries, test_status, temp, coverage, test_file_name) 
    finally:
        semaphore.release()


def main():
    cwd = os.getcwd()

    # Searches all folders in root folder for react components. Tuple with both filename and realtive path of the react components.
    react_files_and_paths = find_react_components.search_files(cwd, ".tsx")

    threads = []
    for file_name, path in react_files_and_paths:

        thread = threading.Thread(target=process_react_component, args=(file_name, path))
        threads.append(thread)
        thread.start()

        semaphore.acquire()
        
    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()
