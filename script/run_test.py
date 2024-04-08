import subprocess

jest_path = "node_modules/jest/bin/jest.js"
eslint_path = "node_modules/eslint/bin/eslint.js"

# Run tests in tests folder.
def run_test(file_name):
  result = subprocess.run(
    ["node", jest_path, f"tests/{file_name}.test.js"], 
    capture_output=True, 
    text=True,
    encoding="utf-8")

  print(result.stderr)

  splitlineshere = result.stderr.splitlines()
  
  if "PASS" in splitlineshere[0]:
    return True, result.stderr
  else:
    return False, result.stderr

# Run eslint on tests.
def run_eslint():
  result = subprocess.run(
      ["node", eslint_path, "tests/**"],
      capture_output=True,
      text=True,
      encoding="utf-8")
  
  print(result.stdout)

# Checks code coverage on the react components.
def check_coverage(files):
  results = subprocess.run(
    ["node", jest_path, "--coverage"], # This is to check all files:  
    # ["node", jest_path, "--coverage", "--collectCoverageFrom=" + ','.join(files)], # This is supposed to only check coverage of react components but does not work
    capture_output=True,
    text=True,
    encoding="utf-8")
  
  print(results.stdout)

'''
Use this if you want to run the script with a certain file to test it without running the whole main script.

jest_path = "node_modules/jest/bin/jest.js"

result = subprocess.run(
  ["node", jest_path, f"../tests/groceryShoppingList.test.js"], 
  capture_output=True, 
  text=True,
  encoding="utf-8")

print(result.stderr)
'''

'''
result = subprocess.run(
    ["node", eslint_path, "tests/**"],
    capture_output=True,
    text=True,
    encoding="utf-8")
  
print(result.stdout)
print()
print(result.stderr)
'''