import file_reader

if __name__ == "__main__":
    file_path = input("Enter the path of the file: ")
    content = file_reader.read_file(file_path)
    if content:
        print("File content:")
        print(content)