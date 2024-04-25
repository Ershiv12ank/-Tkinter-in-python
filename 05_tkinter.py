# this is code for create  frame 

from  tkinter  import *

root = Tk()
root.geometry("444x544")

f1=Frame(root,bg="green",borderwidth=6,relief=SUNKEN)
f1.pack(side=LEFT,fill=Y)
f2=Frame(root,bg="red",borderwidth=6,relief=SUNKEN)
f2.pack(side=TOP,fill=Y)
l=Label(f1,text="project Tkinter-Pycharm")
l.pack(padx=23)
l=Label(f2,text="Frame")
l.pack(padx=233)
root.mainloop()