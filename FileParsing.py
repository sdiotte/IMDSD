# Import Modules
import os

# List of files in current directory
currentdirc = os.getcwd()

Extensions = ['.dat', '.DAT', '.fmt', '.FMT']


def get_file_list(root_dir, F):
    file_list = []
    counter = 1

    for root, dirs, files in os.walk(root_dir):
        for files in files:

            if any(ext in files for ext in F):
                file_list.append(files)
                counter += 1
    return file_list


files = get_file_list(currentdirc, Extensions)
print(files)

# Read/Clean Files


def readfiles(event=None):
    count = 0
    for file in files:
        with open(file, 'r') as infile:
            lines = infile.read().split("#")
            lines = infile.read().splitlines()
            for line in lines:
                if line.startswith("#"):
                    continue
                elif line.startswith(" "):
                    continue
                else:
                    count += 1
                    print(line)
            print(lines)

readfiles()