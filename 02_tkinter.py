from  tkinter  import *
root=Tk()

# Width x Height
root.geometry("644x434")
# width , height 
root.minsize(200,100)
# width , height 
root.maxsize(1200,1000)
lebel=Label(text="This is lable")
lebel.pack()
root.mainloop()