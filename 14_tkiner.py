from  tkinter   import *
import tkinter.messagebox as tmsg
def getdollar():
    print( f"we have creadited {myslider2.get()} dollars to your account")
    tmsg.showinfo("amount credited", f"we have creadited {myslider2.get()} dollars to your account")
root=Tk()
root.geometry("555x555")
root.title("Slider")

Label(root,text="Enter dollar ").pack()
myslider2=Scale(root,from_=0,to=100,orient=HORIZONTAL,tickinterval=20)
myslider2.pack()

Button(root,text="get dollar",pady=10,command=getdollar).pack()
root.mainloop()