import subprocess

def run_test(file_name):


  jest_path = "../node_modules/jest/bin/jest.js"

  result = subprocess.run(
    ["node", jest_path, f"../tests/{file_name}.test.js"], 
    capture_output=True, 
    text=True,
    encoding="utf-8")

  print(result.stderr)