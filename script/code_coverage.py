import subprocess

jest_path = "node_modules/jest/bin/jest.js"

# Checks code coverage on the react components.
def check_coverage_all_tests():
  results = subprocess.run(
    ["node", jest_path, "--coverage"],
    capture_output=True,
    text=True,
    encoding="utf-8")
  
  return parse_coverage_report(results.stdout)

def parse_coverage_report(coverage_result):
    lines = coverage_result.splitlines()
    coverage_data = {}

    for line in lines[4:-1]:  # Skip the header and footer lines
        parts = line.strip().split('|')
        if len(parts) >= 5:  # Ensure that the line contains the expected number of parts
            file_name = parts[0].strip()
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
    
    print(coverage_data)
    return coverage_data

parse_coverage_report('''-------------------------|---------|----------|---------|---------|-------------------
File                     | % Stmts | % Branch | % Funcs | % Lines | Uncovered Line #s
-------------------------|---------|----------|---------|---------|-------------------
All files                |     100 |      100 |     100 |     100 |
 groceryShoppingList.tsx |     100 |      100 |     100 |     100 |
 testMoreFiles.tsx       |     100 |      100 |     100 |     100 |
-------------------------|---------|----------|---------|---------|-------------------''')