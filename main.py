import file_reader
import write_to_gpt
import generate_test_file

if __name__ == "__main__":
    file_path = input("Enter the path of the file: ")
    content = file_reader.read_file(file_path)
    if content:
        test_content = write_to_gpt.call_openai_api(content)
        generate_test_file.generate_test_file(test_content)