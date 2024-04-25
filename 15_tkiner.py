from  tkinter   import *
import tkinter.messagebox as tmsg
root=Tk()
def order():
    tmsg.showinfo("order received ",f"We have received your order for {var.get()}. Thanks for ordering ")

root.geometry("555x555")
root.title("Radio button")

var=StringVar()
var.set("Radio")

Label(root,text="What would you like to have sir ?",font="lucida 19 bold",justify=LEFT,padx=14).pack()
radio=Radiobutton(root,text="Dosa",padx=14,variable=var,value="Dosa").pack(anchor="w")
radio=Radiobutton(root,text="samosa",padx=14,variable=var,value="samosa").pack(anchor="w")
radio=Radiobutton(root,text="jalebi",padx=14,variable=var,value="jalebi").pack(anchor="w")
radio=Radiobutton(root,text="pizza",padx=14,variable=var,value="pizza").pack(anchor="w")

Button(text="Order Now" , command=order).pack()
root.mainloop()