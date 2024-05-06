import subprocess
import os

jest_path = "node_modules/jest/bin/jest.js"
test_folder_path = "tests/"

# Checks code coverage on the react components.
def check_coverage_specific_test(filename):

  testfile_path =  f"{test_folder_path}{filename}"

  results = subprocess.run(
    ["node", jest_path, "--coverage", testfile_path],
    capture_output=True,
    text=True,
    encoding="utf-8")
  return parse_coverage_report(results.stdout, filename)

# Rewrites coverage report to a more suitable form.
def parse_coverage_report(coverage_result, filename):
    lines = coverage_result.splitlines()
    coverage_data = {}
    for line in lines:
      if "All files" in line:
        parts = line.strip().split('|')
        if len(parts) >= 5:   # Ensure that the line contains the expected number of parts
          stmts_coverage = int(parts[1].strip())
          branch_coverage = int(parts[2].strip())
          funcs_coverage = int(parts[3].strip())
          lines_coverage = int(parts[4].strip())

          coverage_data[filename] = {
              'Stmts': stmts_coverage,
              'Branch': branch_coverage,
              'Funcs': funcs_coverage,
              'Lines': lines_coverage
          }

    return coverage_data