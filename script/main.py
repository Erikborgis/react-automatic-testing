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

    # tsx_files = [file for file in os.listdir(folder_path) if file.endswith('.tsx')]

    for file, path in tsx_files_and_paths:
        content = file_reader.read_file(path)
        file_name = os.path.splitext(file)[0]
        if content:
            test_content = write_to_gpt.call_openai_api(content, path)
            generate_test_file.generate_test_file(test_content, file_name)
            run_test.run_test(file_name)
    
    run_test.run_eslint()