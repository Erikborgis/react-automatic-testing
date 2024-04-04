import file_reader
import write_to_gpt
import generate_test_file
import run_test
import os

if __name__ == "__main__":
    folder_path = "../files_to_test"
    tsx_files = [file for file in os.listdir(folder_path) if file.endswith('.tsx')]

    for file in tsx_files:
        content = file_reader.read_file(f"../files_to_test/{file}")
        file_name = os.path.splitext(file)[0]
        if content:
            test_content = write_to_gpt.call_openai_api(content)
            generate_test_file.generate_test_file(test_content, file_name)
            run_test.run_test(file_name)