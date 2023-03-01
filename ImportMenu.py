import tkinter as Tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

def UploadAction(event=None):
    filename = filedialog.askopenfilename()
    print('Selected:', filename)

root = Tk()
frm = ttk.Frame(root, padding=100)
frm.grid()
ttk.Label(frm, text="Upload IMDSD FMT File").grid(column=0, row=0)
ttk.Button(frm, text="FMT", command=UploadAction).grid(column=1, row=0)
ttk.Label(frm, text="Upload IMDSD DAT File").grid(column=0, row=2)
ttk.Button(frm, text="DAT", command=UploadAction).grid(column=1, row=2)
ttk.Label(frm, text="Upload CT2020 FMT File").grid(column=0, row=3)
ttk.Button(frm, text="FMT", command=UploadAction).grid(column=1, row=3)
ttk.Label(frm, text="Upload CT2020 DAT File").grid(column=0, row=4)
ttk.Button(frm, text="DAT", command=UploadAction).grid(column=1, row=4)
ttk.Label(frm, text="Done Uploading").grid(column=0, row=5)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=5)
root.mainloop()