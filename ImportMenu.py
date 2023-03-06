import tkinter as tk
from tkinter import *

def UploadAction(event=None):
    filename = filedialog.askopenfilename()
    print('Selected:', filename)

window = tk.Tk()
#root = Tk()

#Menu Formatting
from tkinter import ttk
from tkinter import filedialog
window.title("Chaintrack Replacement")
for x in range(8):
   for y in range(4):
       frame = tk.Frame(
           master=window,
           relief=tk.RAISED
       )

#Menu Buttons
frame.grid(row=x, column=y)
tk.Label(frame, text =f'\t\t\t\tChaintrack Replacement', font=('TkDefaultFont', 20)).grid (column=1, row=0) 
tk.Label(frame, text=f"\n\nUpload IMDSD FMT File\n\n", font= "1").grid(column=1, row=1)
tk.Button(frame, text="FMT", command=UploadAction, font= "1").grid(column=2, row=1)
tk.Label(frame, text=f"\n\nUpload IMDSD DAT File\n\n", font= "1").grid(column=1, row=2)
tk.Button(frame, text="DAT", command=UploadAction, font= "1").grid(column=2, row=2)
tk.Label(frame, text=f"\n\nUpload CT2020 FMT File\n\n", font= "1").grid(column=1, row=3)
tk.Button(frame, text="FMT", command=UploadAction, font= "1").grid(column=2, row=3)
tk.Label(frame, text=f"\n\nUpload CT2020 DAT File\n\n", font= "1").grid(column=1, row=4)
tk.Button(frame, text="DAT", command=UploadAction, font= "1").grid(column=2, row=4)
tk.Label(frame, text=f"\n\nDone Uploading\n\n", font= "1").grid(column=1, row=5)
tk.Button(frame, text="Quit", command=window.destroy, font= "1").grid(column=2, row=5)

#Menu Checkbuttons
tk.Checkbutton(frame, text = 'Parse IMDSD', onvalue = 1, offvalue = 0).grid(column=0, row=7)
tk.Checkbutton(frame, text = f'Parse CT2020', onvalue = 1, offvalue = 0).grid(column=1, row=7)
tk.Checkbutton(frame, text = 'Parse and Compare Both', onvalue = 1, offvalue = 0).grid(column=2, row=7)
tk.Checkbutton(frame, text = 'Developer File', onvalue = 1, offvalue = 0).grid(column=3, row=7)

window.mainloop()