import subprocess
import os

jest_path = "node_modules/jest/bin/jest.js"

# Checks code coverage on the react components.
def check_coverage_specific_test(testfile_path):
  results = subprocess.run(
    ["node", jest_path, "--coverage", testfile_path],
    capture_output=True,
    text=True,
    encoding="utf-8")
  
  return parse_coverage_report(results.stdout, testfile_path)

def parse_coverage_report(coverage_result, testfile_path):
    testfile_name = os.path.basename(testfile_path)
    print(f"Testfilename: {testfile_name}")
    lines = coverage_result.splitlines()
    coverage_data = {}
    for line in lines[4:-1]:  # Skip the header and footer lines
        parts = line.strip().split('|')
        if len(parts) >= 5:  # Ensure that the line contains the expected number of parts
            file_name = f"{testfile_name}"
            stmts_coverage = int(parts[1].strip())
            branch_coverage = int(parts[2].strip())
            funcs_coverage = int(parts[3].strip())
            lines_coverage = int(parts[4].strip())

            coverage_data[file_name] = {
                'Stmts': stmts_coverage,
                'Branch': branch_coverage,
                'Funcs': funcs_coverage,
                'Lines': lines_coverage
            }
    
    return coverage_data