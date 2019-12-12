from tkinter import *
############### Form colors & fonts ################
fg="gold"
bg="purple"
f1="Times 16 bold"
f2="Times 14 bold"
f3="Times 14"
####################################################
######### Event Handlers ##################
def Close():
    #quit()
    myForm.destroy()
def Process():
    strName = entCustName.get() #retrieves contents of Entry control
    strName= strName.title()  #force to title format
    lblCopy["text"] = strName
def Reset():
    entCustName.delete(0,END)
    lblCopy["text"] = ""
    entCustName.focus()
myForm = Tk()  #create empty form
myForm.title("STEVE's AUTO SALES") #set title bar text
myForm.geometry("800x600") #sets form width and height
#myForm["bg"] = "sky blue"
myForm.configure(bg=bg)

lblCompName = Label(text="STEVE's AUTO SALES",fg=fg,bg=bg,font=f1)
lblCompName.place(x=250,y=10)
lblCustName = Label(text="Customer Name:",fg=fg,bg=bg,font=f3)
lblCustName.place(x=150,y=100)
entCustName = Entry(bg="white",fg=fg,font=f3,width=25)
entCustName.place(x=300,y=100)
lblCopy = Label(text="",bg=bg,fg="red",font=f3)
lblCopy.place(x=300,y=200)
btnProcess = Button(text="Process",bg=bg,fg=fg,font=f2,width=8,command=Process)
btnProcess.place(x=370,y=500)
btnReset = Button(text="Reset",bg=bg,fg=fg,font=f2,width=8,command=Reset)
btnReset.place(x=485,y=500)
btnClose = Button(text="Close",bg="red",fg="white",font=f2,width=8,command=Close)
btnClose.place(x=600,y=500)
entCustName.focus()
myForm.mainloop() #shows form and gives user interface control



