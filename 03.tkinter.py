from  tkinter  import *
from PIL import Image ,ImageTk
root=Tk()
root.geometry("500x600")
photo=PhotoImage(file="1.png.png")
# extra code
image=Image.open("photo.jpg")
photo=ImageTk.PhotoImage(image)
label=Label(image=photo)
label.pack()
root.mainloop()