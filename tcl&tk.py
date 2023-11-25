'''
tcl is a dynamic interpreted programming language
tk is tcl package . adds custom commond
themed tk a new family of tk widgets


MODULS 
1.ttk
2. colorchooser

'''

import tkinter
from tkinter import ttk
import tkinter.colorchooser

win = tkinter.Tk()
win.title("Color choose window")

def changecolor():
    color=tkinter.colorchooser.askcolor()
    win.configure(bg=color[1])
ttk.Button(win,text="pick color",command=changecolor).pack()
    
win.mainloop()