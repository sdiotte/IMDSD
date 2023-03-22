#Import Modules
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import os.path
import shutil

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
