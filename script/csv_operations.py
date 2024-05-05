import csv

statistics_folder = "statistics/"

# Generates a csv file, provides statistics of the unit test generation.
def generate_csv_file(file_name):
    csv_filename = f"{statistics_folder}{file_name}_stats.csv"
    with open(csv_filename, 'w', newline='') as csvfile:
        fieldnames = ['File Name', 'Number of Tries', 'Pass Status', 'Stmts', 'Branch', 'Funcs', 'Lines', 'Temperature']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

# Add a unit test generation to the statistics file.
def append_to_csv_files(file_name, number_of_tries, pass_status, temperature, coverage, test_file_name):
    csv_filename = f"{statistics_folder}{file_name}_stats.csv"
    with open(csv_filename, 'a', newline='') as csvfile:
        fieldnames = ['File Name', 'Number of Tries', 'Pass Status', 'Stmts', 'Branch', 'Funcs', 'Lines', 'Temperature']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({
            'File Name': f"{test_file_name}",
            'Number of Tries': number_of_tries,
            'Pass Status': "Pass" if pass_status else "Fail",
            'Stmts': coverage[test_file_name].get('Stmts', "NA"),
            'Branch': coverage[test_file_name].get('Branch', "NA"),
            'Funcs': coverage[test_file_name].get('Funcs', "NA"),
            'Lines': coverage[test_file_name].get('Lines', "NA"),
            'Temperature': temperature
        })

        print(f"Stats for '{test_file_name}' written to '{csv_filename}'.")
