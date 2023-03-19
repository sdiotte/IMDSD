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

def readfiles(event=None):
    
    for filename in files:
        with open (filename, 'r+') as file:
            print(file.read())

readfiles()






#with open ():
   # contents = dat.read()
    #print(contents)

#Import FMT File
#with open('*.FMT') as fmt:
   # contents = fmt.read()
    #print(contents)
