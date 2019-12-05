from tkinter import *

############ Form Color & fonts ####################
fg="navy"
bg="sky blue"
f1="Arial 16 bold"
f2="Arial 14 bold"
f3="Arial 14"

####################################################
myForm = Tk() #create empty form
myForm.title("Steve's Application") #set title bar text
myForm.geometry("800x600") #sets size
#myForm["bg"] = "sky blue"
myForm.configure(bg=bg)

lblCompName = Label(text="STEVE's AUTO SAKES",fg=fg,bg=bg,font=f1)
lblCompName.place(x=250,y=10)

lblCustName = Label(text="Customer Name:",fg=fg,bg=bg,font=f3)
lblCustName.place(x=150,y=100)

entCustName = Entry(bg="white",fg=fg,font=f3,width=25)
entCustName.place(x=300,y=100)


myForm.mainloop() #shows form
