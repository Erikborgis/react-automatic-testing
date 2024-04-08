import csv

def generate_csv_file(file_name):
    csv_filename = f"{file_name}_stats.csv"
    with open(csv_filename, 'w', newline='') as csvfile:
        fieldnames = ['File Name', 'Number of Tries', 'Pass Status', '% Stmts', '% Branch', '% Funcs', '% Lines', 'Temperature']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

def append_to_csv_files(file_name, test_generation_statistics, coverage, temperature_file_name):
    print(f"Test File name: {temperature_file_name}.test.js")
    csv_filename = f"{file_name}_stats.csv"
    with open(csv_filename, 'a', newline='') as csvfile:
        fieldnames = ['File Name', 'Number of Tries', 'Pass Status', '% Stmts', '% Branch', '% Funcs', '% Lines', 'Temperature']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({
            'File Name': f"{temperature_file_name}.test.js",
            'Number of Tries': test_generation_statistics[0],
            'Pass Status': "Pass" if test_generation_statistics[1] else "Fail",
            '% Stmts': coverage[f"{temperature_file_name}.test.js"]['Stmts'],
            '% Branch': coverage[f"{temperature_file_name}.test.js"]['Branch'],
            '% Funcs': coverage[f"{temperature_file_name}.test.js"]['Funcs'],
            '% Lines': coverage[f"{temperature_file_name}.test.js"]['Lines'],
            'Temperature': test_generation_statistics[2]
        })
        print(f"Stats for '{temperature_file_name}.test.js' written to '{csv_filename}'.")
