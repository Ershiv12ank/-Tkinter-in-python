from tkinter import *
def getvals():
    print(f"The value of usernames is {userentry}")
    print(f"The value of password is {passwordentry}")
root=Tk()
root.geometry("444x888")
user=Label(root,text="username")
password=Label(root,text="Password")
user.grid()
password.grid(row=1)

# variable class es in tkinter
# BooleanVar, DoubleVar, Intvar,StringVal
uservalue=StringVar()
passwordvalue=StringVar()
userentry=Entry(root,textvariable=uservalue)
passwordentry=Entry(root,textvariable=passwordvalue)
userentry.grid(row=0,column=1)
passwordentry.grid(row=1,column=1)

Button(text="submit",command=getvals).grid()

root.mainloop()