import file_reader
import write_to_gpt
import generate_test_file
import run_test
import find_react_components
import os

if __name__ == "__main__":
    
    cwd = os.getcwd()

    # Searches all folders in root folder for react components. Tuple with both filename and realtive path of the react components.
    tsx_files_and_paths = find_react_components.search_files(cwd, ".tsx")

    # tsx_files = [file for file in os.listdir(folder_path) if file.endswith('.tsx')] Solution for only generating tests for components in certain folder.

    for file, path in tsx_files_and_paths:
        react_component_text = file_reader.read_file(path)
        file_name = os.path.splitext(file)[0]
        if react_component_text:
            test_content = write_to_gpt.call_openai_api(react_component_text, path)
            
            # Regenerates unit tests until the tests pass. Max 10 tries.
            number_of_tries = 0
            while(True and number_of_tries < 10):
                generate_test_file.generate_test_file(test_content, file_name)
                
                # If the test does not return any errors then break the loop.
                test_status_message = run_test.run_test(file_name)
                if(test_status_message):
                    test_content = write_to_gpt.regenerate_test(react_component_text, test_content, test_status_message, path)
                    number_of_tries += 10
                else:
                    break
    
    run_test.run_eslint()
    run_test.check_coverage([filename for filename, _ in tsx_files_and_paths])