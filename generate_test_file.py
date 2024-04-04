import os

# Fix so method retrieves component name.
def generate_test_file(content):
    test_folder = "tests"
    if not os.path.exists(test_folder):
        os.makedirs(test_folder)
    
    # File should be called "nameofcomponent.test.js"
    file_path = os.path.join(test_folder, f"test.test.js")
    
    with open(file_path, "w") as test_file:
        test_file.write(content)
        
    print(f"{file_path} generated successfully!")