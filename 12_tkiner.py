from tkinter import *
def myfunc():
    print("This is a demo file ")
root=Tk()
root.geometry("444x888")
mymenu=Menu(root)
mymenu.add_command(label="File",command=myfunc)
mymenu.add_command(label="Exit",command=quit)
root.config(menu=mymenu)
root.mainloop()