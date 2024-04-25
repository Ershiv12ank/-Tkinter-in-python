from tkinter import *
def getvals():
    print("It works")
root=Tk()
root.geometry("444x888")
lable=Label(root,text="This is form",font="comicsansms 13 bold").grid(row=0 , column=3)
name=Label(root,text="Name")
phone=Label(root,text="phone")
Gender=Label(root,text="Gender")
emergency=Label(root,text="emergency")
Paymentmode=Label(root,text="Payment mode")

name.grid(row=1,column=2)
phone.grid(row=2,column=2)
Gender.grid(row=3,column=2)
emergency.grid(row=4,column=2)
Paymentmode.grid(row=5,column=2)

namevalue=StringVar()
phonevalue=StringVar()
Gendervalue=StringVar()
emergencyvalue=StringVar()
Paymentmodevalue=StringVar()
foodservicesvalue=IntVar()

nameentry=Entry(root,textvariable=namevalue)
phoneentry=Entry(root,textvariable=phonevalue)
Genderentry=Entry(root,textvariable=Gendervalue)
emergencyentry=Entry(root,textvariable=emergencyvalue)
Paymentmodeentry=Entry(root,textvariable=Paymentmodevalue)

nameentry.grid(row=1 ,column=3)
phoneentry.grid(row=2 ,column=3)
Genderentry.grid(row= 3,column=3)
emergencyentry.grid(row= 4,column=3)
Paymentmodeentry.grid(row=5 ,column=3)


foodservice=Checkbutton(text="Want to prebook your meals ?",variable=foodservicesvalue)
foodservice.grid(row=6,column=3)

Button(text="Submit to Harry Treavel" ,command=getvals).grid(row=7,column=3)
root.mainloop()