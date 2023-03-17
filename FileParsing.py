#Import Modules
import os


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

#Read Files
#def readfiles(event=None):
   # with open (files, 'r') as file:
    #    counter += 1
     #   print(file.read())

#readfiles(files)




#with open ():
   # contents = dat.read()
    #print(contents)

#Import FMT File
#with open('*.FMT') as fmt:
   # contents = fmt.read()
    #print(contents)

#add code: if file is fmt, remove #'s and anything after...perhaps have it import the old fields and place under new fields on header. Maybe with acronym for system in the front with dot or dash

    
#DAT to FMT Array
#dat_to_fmt = []*