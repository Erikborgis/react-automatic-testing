import subprocess

jest_path = "node_modules/jest/bin/jest.js"
eslint_path = "node_modules/eslint/bin/eslint.js"
test_folder_path = "tests/"

# Run tests in tests folder.
def run_test(file_name):
    # Construct the command to run Jest with the specified test file
    command = ["node", jest_path, f"{test_folder_path}{file_name}"]

    # Run the command and capture the output
    result = subprocess.run(command, capture_output=True, text=True, encoding="utf-8")
    
    # Split the output into lines
    split_lines = result.stderr.splitlines()

    # Check if the test passed based on the output
    return "PASS" in split_lines[0] if split_lines else False, result.stderr
