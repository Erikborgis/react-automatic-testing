# Currently hardcoded filepath!!

import subprocess

def run_test(test_file):


  jest_path = "../../node_modules/jest/bin/jest.js"

  result = subprocess.run(
    ["node", jest_path, "../tests/test.test.js"], 
    capture_output=True, 
    text=True,
    encoding="utf-8")

  print(result.stderr)
  print(result.stdout)