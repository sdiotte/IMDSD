import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import ttk

window = tk.Tk()

#Defining Functions
def menu_bar(): 
    pass

def IMDSD_UploadAction(event=None):
    for x in range(2):
        filename = filedialog.askopenfilename(title='IMDSD Files')
        print('Selected:', filename)
    IMDSD_Reports = IMDSD()
    Developer_File = Developer()
    
def CT2020_UploadAction(event=None):
    for x in range(2):
        filename = filedialog.askopenfilename(title='CT2020 Files')
        print('Selected:', filename)
        CT2020_Reports = CT2020()
        Developer_File = Developer()

def Systems_UploadAction(event=None):
    for x in range(2):
        filename = filedialog.askopenfilename(title='IMDSD Files')
        print('Selected:', filename)
    for x in range(2):
        filename = filedialog.askopenfilename(title='CT2020 Files')
        print('Selected:', filename)
        Both_Reports = IMDSD()
        Developer_File = Developer()

def IMDSD(event=None):
    pass
#car = {
  #"brand": "Ford",
 # "model": "Mustang",
 # "year": 1964
#}

#x = car.get("model")

#print(x)

def CT2020(event=None):
    pass

def Both(event=None):
    pass

def Developer(event=None):
    top = Toplevel(window)
    top.title('Developer File')
    label.Label(top, text="Do you need a Developer File with this as well?", font=("Courier 22 bold"))
    label.pack()
#Create an Entry widget to accept User Input
    global entry
    entry= Entry(top, width= 40)
    entry.focus_set()
    entry.pack()
    string= entry.get()
    label.configure(text=string)
#Create a Button to validate Entry Widget
    ttk.Button(top, text= "Done",width= 20, command=Developer).pack(pady=20)

#Menu Window Formatting
window.title("Chaintrack Replacement")

#Menubar Formmatting
menubar=tk.Menu(window)
menu_file=tk.Menu(menubar, tearoff=0)

menubar.add_cascade(label='File',menu=menu_file)

#Submenu Formatting
submenu_upload=tk.Menu(menu_file, tearoff=0)
submenu_upload= Menu(menu_file, tearoff=0)
submenu_upload.add_command(label="IMDSD DAT & FMT", command=IMDSD_UploadAction)
submenu_upload.add_command(label="CT2020 DAT & FMT", command=CT2020_UploadAction)
submenu_upload.add_command(label="Both", command=Systems_UploadAction)
menu_file.add_cascade(label='Upload', menu=submenu_upload)

menu_file.add_command(label='Exit', command=window.destroy)

window.config(menu=menubar)

window.mainloop()
