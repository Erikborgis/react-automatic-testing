import os

# Returns tuple
def search_files(directory, extension):
    found_files = []
    for root, dirs, files in os.walk(directory):
        if 'node_modules' in dirs:
            dirs.remove('node_modules')
        for file in files:
            if file.endswith(extension):
                # Get the relative path of the file
                relative_path = os.path.relpath(os.path.join(root, file), directory)
                # Split the relative path and remove the first part (directory)
                _, relative_path = os.path.splitdrive(relative_path)
                # Append a tuple of filename and relative path
                found_files.append((os.path.splitext(file)[0], relative_path))

    if not(found_files):
        print("No .tsx files found.")
    
    return found_files