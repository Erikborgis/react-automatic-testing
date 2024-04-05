import os

def generate_test_file(content, file_name):
    test_folder = "tests"
    if not os.path.exists(test_folder):
        os.makedirs(test_folder)
    
    file_path = os.path.join(test_folder, f"{file_name}.test.js")
    
    with open(file_path, "w") as test_file:
        test_file.write(content)
        
    print(f"{file_path} generated successfully!")