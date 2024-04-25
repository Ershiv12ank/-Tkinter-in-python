from  tkinter  import *
root=Tk()
root.geometry("644x434")
3 #title
root.title("This is a title")
# important Label Option

#text-Add the text
#bd-backgroung
#fg-foreground
#font - sets the font font=("comicsansms",19,"bold")  or font="comicsansms 19 bold"
#padix-x padding
#pady-y padding
# relief - border styling - Sunken , Raised , groove , ride

# title lable
title_label=Label(text="Shivank pandey",bg='pink' , fg="black",padx=10,pady=20,font="comicsansms 19 bold",borderwidth=5,relief=SUNKEN)


# important pack
#fill
#padx
#pady

#title_label.pack(side=BOTTOM , anchor="e")
title_label.pack(side=BOTTOM , anchor="e",fill=X)
root.mainloop()