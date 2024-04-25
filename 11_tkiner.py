# event hanling 

from tkinter import *
def harry(event):
    print(f"you clicked on the button at {event.x},{event.y}")
root=Tk()
root.title("Event")
root.geometry("444x888")
widget=Button(root,text="Plese Click me ")
widget.pack()

widget.bind('<Button-1>',harry)

root.mainloop()