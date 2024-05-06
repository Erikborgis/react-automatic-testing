import os

# Creates a test file in the tests folder.
def create_test_file(content, file_name):
    test_folder = "tests"
    if not os.path.exists(test_folder):
        os.makedirs(test_folder)
    
    file_path = os.path.join(test_folder, file_name)
    
    with open(file_path, "w") as test_file:
        test_file.write(content)
        
    print(f"{file_path} created successfully!")

# Reads file at certain path and returns string.
def read_file(file_path):
    print(file_path)
    try:
        with open(file_path, 'r') as file:
            text = file.read()
        return text
    except FileNotFoundError:
        print("File not found in read_file method")
    except Exception as e:
        print("An error occurred:", e)
