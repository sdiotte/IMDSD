# Import Modules
import os
from contextlib import redirect_stdout

# List of files in current directory
currentdirc = os.getcwd()

Extensions = ['.dat', '.DAT', '.fmt', '.FMT']


def get_file_list(root_dir, F):
    file_list = []
    counter = 0

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
        with open(file, 'r+') as infile:
            lines = infile.read().splitlines()
            for line in lines:
                pound_loc = line.find("#")
                if pound_loc > -1:
                    line = line[:pound_loc]
                if line.startswith("#"):
                    continue
                elif (len(line.strip()) == 0):
                    continue
                else:
                    count += 1
                    print(line)
                    infile.write(line)
            infile.truncate()
readfiles()