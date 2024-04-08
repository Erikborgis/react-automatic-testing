import csv

def generate_csv_files(test_generation_statistics, coverage):
    for file_name, num_tries, pass_status in test_generation_statistics:
        csv_filename = f"{file_name}_stats.csv"
        with open(csv_filename, 'w', newline='') as csvfile:
            fieldnames = ['File Name', 'Number of Tries', 'Pass Status', '% Stmts', '% Branch', '% Funcs', '% Lines']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({
                'File Name': file_name,
                'Number of Tries': num_tries,
                'Pass Status': "Pass" if pass_status else "Fail",
                '% Stmts': coverage[file_name]['Stmts'],
                '% Branch': coverage[file_name]['Branch'],
                '% Funcs': coverage[file_name]['Funcs'],
                '% Lines': coverage[file_name]['Lines']
            })
        print(f"Stats for '{file_name}' written to '{csv_filename}'.")

# Example usage:
# generate_csv_files(test_generation_statistics, coverage)
