from tkinter import *
root=Tk()
root.geometry("444x666")

def hello():
    print("thank you to click")
frame= Frame(root,borderwidth=7,bg="RED",relief=SUNKEN)
frame.pack(side=LEFT,anchor="nw")

b1=Button(frame,fg="blue",text="click now",command=hello)
b1.pack(side=LEFT,padx=23)

b1=Button(frame,fg="blue",text="click Now",command=hello)
b1.pack(side=LEFT,padx=23)

b2=Button(frame,fg="blue",text="click Now",command=hello)
b2.pack(side=LEFT,padx=23)

b3=Button(frame,fg="blue",text="click Now",command=hello)
b3.pack(side=LEFT,padx=23)

root.mainloop()