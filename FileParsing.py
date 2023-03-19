#Import Modules
import os,glob

#List of files in current directory
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

#Read/Write Files
def readfiles(event=None):
    
    for filename in files:
        with open(filename, 'r') as infile:
            file = infile.read()
            file = file.split('#', 1)[0] #START here to remove everything after '#' line by line
        with open(filename, 'w') as outfile:
            outfile.write(file)
            print(file)

readfiles()

#Clean Files
def cleanfiles(event=None):
    #for filename in files:
        #filename.replace('#','')
        #print(filename)
        pass