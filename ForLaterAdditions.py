#Import Modules
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import os.path
import shutil
import pandas as pd

window = tk.Tk()

#Defining Functions
def UploadAction(file_type):
    for x in range(2):
        file = filedialog.askopenfilename(title=file_type)
        filename = os.path.basename(file)
        filetitle, fileext = os.path.splitext(filename)      
        currentdirc = os.getcwd()
        filepath = os.path.join(currentdirc, filename)
        shutil.copy(file, filepath)
    if file_type == 'IMDSD':
        reports = IMDSD()
    elif file_type == 'CT2020':
        reports = CT2020()
    window.destroy()

def Systems_UploadAction(event=None):
    for x in range(2):
        filename = filedialog.askopenfilename(title='IMDSD Files')
        print('Selected:', filename)
    for x in range(2):
        filename = filedialog.askopenfilename(title='CT2020 Files')
        print('Selected:', filename)
        Both_Reports = IMDSD()

def IMDSD(event=None):
    print('IMDSD')

def CT2020(event=None):
    print('CT2020')

def Both(event=None):
    pass

#Menu Window Formatting
window.title("Chaintrack Replacement")
window.geometry("300x25")
window.eval('tk::PlaceWindow . center')

#Menubar Formmatting
menubar=tk.Menu(window)
menu_file=tk.Menu(menubar, tearoff=0)

menubar.add_cascade(label='File', menu=menu_file)

#Submenu Formatting
submenu_upload=tk.Menu(menu_file, tearoff=0)
submenu_upload= Menu(menu_file, tearoff=0)
#upload()
submenu_upload.add_command(label="IMDSD DAT & FMT", command=lambda: UploadAction('IMDSD'))
submenu_upload.add_command(label="CT2020 DAT & FMT", command=lambda: UploadAction('CT2020'))
submenu_upload.add_command(label="Both", command=Systems_UploadAction)
menu_file.add_cascade(label='Upload', menu=submenu_upload)

menu_file.add_command(label='Exit', command=window.destroy)

window.config(menu=menubar)

window.mainloop()

# Initialize an empty dictionary to store the results
result_dict = {}
# Open the FMT file with the given name for reading
f = open("BATERR.FMT", "r")
# Initialize a counter to track LITERAL occurrences
batch_count = 0
store_count = 0
literal_count = 0
crlf_count = 0
# Loop through each line in the file
for line in f:
  # Check if the first character of the line is a letter (indicating a field)
  if line[0].isalpha():
    # Remove any leading and trailing whitespaces from the line
    line = line.strip()
    # If the line matches the specific string "RECORD_TYPE BATCH_LINE", skip to the next iteration
    if line == "RECORD_TYPE BATCH_LINE":
        continue
    # Find the position of the '#' character (indicating the start of a comment)
    pound_loc = line.find("#")
    # If a comment is found, remove it from the line
    if pound_loc != -1:
        line = line[:pound_loc]
    # Split the line to extract the key (field name)
    key = line.split()[0]
    # Extract the value (field format) by removing the key from the line and stripping whitespaces
    value = line.replace(key, "").strip()
    # If the key is "BATCH.BATCH_NUMBER", append the current literal_count to the key and increment the count
    if key == "BATCH.BATCH_NUMBER":
        key = f"{key}{batch_count}"
        batch_count += 1
    # If the key is "STORE.STORE_NUMBER", append the current literal_count to the key and increment the count
    if key == "STORE.STORE_NUMBER":
        key = f"{key}{store_count}"
        store_count += 1  
    # If the key is "LITERAL", append the current literal_count to the key and increment the count
    if key == "LITERAL":
        key = f"{key}{literal_count}"
        literal_count += 1
    # If the key is "CRLF", append the current literal_count to the key and increment the count
    if key == "CRLF":
        key = f"{key}{crlf_count}"
        crlf_count += 1
    # Add the key-value pair to the result dictionary
    result_dict[key] = value

    
result_dict

#further processing for length of fields and transforming str nums to ints
for key, value in result_dict.items():
    if value.startswith('"') and value.endswith('"'):
        str_value = value.strip('"')
        if str_value.isdigit():
            result_dict[key] = len(str_value)
        else:
            result_dict[key] = len(str_value)
    elif value.isdigit():
        result_dict[key] = int(value)

#Create header dictionary
hdr_keys = [
    "BATCH.BATCH_NUMBER0",
    "LITERAL0",
    "LITERAL1",
    "LITERAL2",
    "STORE.DIVISION_NUMBER",
    "LITERAL3",
    "STORE.STORE_NUMBER0",
    "LITERAL4",
    "LITERAL5"
]
hdr_dict  = result_dict
hdr_dict = {key: result_dict[key] for key in hdr_keys}
hdr_dict["BATCH.BATCH_NUMBER0"] = 6 
hdr_dict

#Create table dictionary
table_keys = [
    "BATCH.BATCH_NUMBER1",
    "BATCH.HOST_SEQ",
    "LITERAL6",
    "BATCH_LINE.TABLE",
    "BATCH_OP",
    "LITERAL7",
    "BATCH_LINE.ERR_CODE",
    "LITERAL8",
    "STORE.STORE_NUMBER1",
    "PRIMARY_KEY"
]
table_dict  = result_dict
table_dict = {key: result_dict[key] for key in table_keys}
table_dict["BATCH.BATCH_NUMBER1"] = 6 
table_dict["BATCH.HOST_SEQ"] = 6
table_dict

#Create header dataframe and CSV
hdr_df = pd.DataFrame()
pd.set_option('display.colheader_justify', 'center')
f = open("BATERRCT.DAT", "r")
#For header lines:
for line in f:
    if "HDR" in line:
        result_dict = {}
        for key, field_len in hdr_dict.items():
            value = line[:field_len]
            line=line[field_len:]
            #To keep spaces for field len validation
            if value.isspace():
                value = f'"{value}"'
            result_dict[key]=[value]
        hdr_df = pd.concat([
            pd.DataFrame(result_dict), hdr_df
        ])
        hdr_df.sort_values(by=["BATCH.BATCH_NUMBER0"], ascending=True, inplace=True)
        hdr_df.reset_index(drop=True, inplace=True)
        hdr_df.index = hdr_df.index + 1
hdr_df.to_csv('IMDSD_BATERR.csv')
print(hdr_df)
hdr_df

#Create table dataframe and append to CSV
table_df = pd.DataFrame()
pd.set_option('display.colheader_justify', 'center')
f = open("BATERRCT.DAT", "r")
# For table lines:
for line in f:
    if "HDR" not in line:
        result_dict = {}
        for key, field_len in table_dict.items():
            value = line[:field_len]
            line=line[field_len:]
            #To keep spaces for field len validation
            if value.isspace():
                value = f'"{value}"'
            result_dict[key]=[value]
        table_df = pd.concat([
            pd.DataFrame(result_dict), table_df
        ])
        table_df.replace('"\n"', float("Nan"), inplace=True)
        table_df.dropna(inplace=True)
        table_df.sort_values(by=["BATCH.BATCH_NUMBER1", "BATCH.HOST_SEQ"], ascending=True, inplace=True)
        table_df.reset_index(drop=True, inplace=True)
        table_df.index = table_df.index + 1
table_df.to_csv('IMDSD_BATERR.csv', mode='a', header=True)
print(table_df)
table_df
