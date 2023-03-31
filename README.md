# IMDSD
Code Kentucky Python 1 Project

<!-- Project Brief: -->
According to Ocrolus.com, 75% of data loss is caused by human error and 58% of service downtime is attributable to human mistakes. During a system replacement project, the need for accuracy is especially important when mapping the legacy system to the replacement system. Rarely, are two systems identical, requiring many hours to be spent analyzing the two systems, their data and the needs of the business this system supports. Errors during this phase of the project can cause fundamental errors down the road, leading to hours of troubleshooting and downtime.

I believe we can greatly reduce the amount of downtime and troubleshooting hours by automating 95% of data sanity checks performed during system replacement projects. This project stops human data entry errors from occurring as the Baterr DAT file lines are parsed by it's FMT file, and it's just the beginning!  


<!-- Packages: -->
Please refer to the requirements.txt file for relevant packages you will need to install to run this. 


<!-- Features: -->
The project required features that I utilized during the making of this. 

* Make a list, dictionary, tuple, or other standard python data structure to read in data for your program.
    -Result_dict: Reads, parses and cleans the FMT file. Leaving a dictionary containing the field names (key) and their lengths (value) behind. 


* Read in data from a local csv, excel file, json, or any other file type.
    -FMT File - This is a local flat file which is moved to the project directory by the UploadAction function of the tkinter menu and read/manipulated into the result_dict

    -DAT File - This is a local flat file which is moved to the project directory by the UploadAction function of the tkinter menu and read/manipulated into the two pd.DataFrames


* Use custom functions or lambdas to perform specific operations to clean or manipulate your data, return those values, then use them in other parts of your project.
    -UploadAction() - is used for the user to load their files and to move the files to the projects directory

    -lambada - is used in the tkinter's upload command, this is more a future feature so that the system file utilized can be identified and the proper UploadAction() will be identified (there will be two)


* Use built-in pandas or numpy functions to do things like remove 0’s and null values where they don’t belong in your dataset.
    -pd.concat - is used when creating the DataFrames to apply the result_dict


* Use at least 5 different built-in Python functions to find out something about your data.
    -len - is used throughout this project; to get the length of the literal fields that contain only spaces and in the creation of the DataFrames to parse the DAT file.

    -strip - used when cleaning the FMT file, in order to find out the correct length of the literal fields. 

    -str.isdigit() - is used in this project; to find out if a field is a number.

    -str.isalpha() - is used in this project; to find out if a field is a string.

    -isspace() - is used in the creation of the DataFrames to identify if the field contains all spaces, so quotations can be put around them to keep them when these are saved to a csv.


* Use a GUI library like tkinter to make an interactive visualization.
    - A tkinter menu has been created for the user to upload their flat files, this also copies the files they have selected from their directory to the projects directoy. 



<!-- Instructions: -->
You can clone this repository to any directory on your computer. 
    Note: When uploading the FMT and DAT files, this will copy those files from the directory you currently have them in to the project directory. 

Before you run ImportMenu.py, save the FMT and DAT files to a directory other than the project's. 
    Note: This is because those utilizing this would be opening these files from another directory on their computer. 

After saving you will need to open and run ImportMenu.py
    - Open this in the IDE or source code editor of choice
        Note: As long as this supports Python

When the Chaintrack Replacement Menu appears: 
    - Click on File
    - Click on Upload 
    - Select IMDSD DAT & FMT
    - In the pop-up window, go to the directory where you saved the DAT and FMT files
    - Open both files, one at a time
        Notes: 
            -These don't need to be uploaded in any particular order, you just want to make sure you have one DST and one FMT
            -The menu will close automatically once you have uploaded the second file

Once this has finished running (less than a minute):
    -Open the directory where you saved the project
    -Locate your parsed data by opening the IMDSD_BATERR.csv file
        Note: The header (HDR) lines are first in the file followed by the table lines (the DAT file furnished here contains Supplier [SUP] lines)


<!-- Data: -->
.DAT - Files with this extension are automatically generated flat files containing binary text for a program or application, these are accompanied by FMT files. 

.FMT - Files with this extension are flat files used to tell a system and users what the format of the .dat file is. 

BATERR - This is a file that contains all of the errors identified by the system in regards to daily hostmnt loads (i.e. supplier, item, packaging, dept info and more)



