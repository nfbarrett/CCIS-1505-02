# Programer: Nick Barrett
# Date Written: Dec 10, 2019
# Program Name: P11.py
# Company Name: HTC-CCIS1505



from tkinter import *
############### Form colors & fonts ################
fg="blue"
bg="sky blue"
f1="Helvetica 16 bold"
f2="Helvetica 12 bold"
f3="Helvetica 12"
####################################################
######### Event Handlers ##################

### show="*" john doe fopwpo
def Login():
    blnDone = False
    while blnDone == False:
        str_name = entCustName.get() #retrieves contents of Entry control
        str_pass = entCustPass.get()
        if str_name == "john doe" and str_pass == "fopwpo":
            lblCopy["text"] = "Login successful"
            blnDone = True
        else:
            lblCopy["text"] = "LoginID or Password Invalid"
            blnDone = True
    
def Clear():
    entCustName.delete(0,END)
    entCustPass.delete(0,END)
    lblCopy["text"] = ""
    entCustName.focus()
myForm = Tk()  #create empty form
myForm.title("LOGIN") #set title bar text
myForm.geometry("580x380") #sets form width and height
#myForm["bg"] = "sky blue"
myForm.configure(bg=bg)

lblCompName = Label(text="HTC PHONES SALES",fg=fg,bg=bg,font=f1)
lblCompName.place(x=168,y=25)

lblCompName = Label(text="Application Login",fg=fg,bg=bg,font=f1)
lblCompName.place(x=180,y=60)

lblCustName = Label(text="LoginID:",fg=fg,bg=bg,font=f3)
lblCustName.place(x=180,y=130)

entCustName = Entry(bg=bg,fg=fg,font=f3,width=25)
entCustName.place(x=255,y=130)

lblCustPass = Label(text="Password:",fg=fg,bg=bg,font=f3)
lblCustPass.place(x=168,y=180)

entCustPass = Entry(bg=bg,fg=fg,font=f3,width=25,show="*")
entCustPass.place(x=255,y=180)


lblCopy = Label(text="",bg=bg,fg="red",font=f3)
lblCopy.place(x=275,y=230)

btnProcess = Button(text="Login",bg=bg,fg=fg,font=f2,width=8,command=Login)
btnProcess.place(x=375,y=300)
btnReset = Button(text="Clear",bg=bg,fg=fg,font=f2,width=8,command=Clear)
btnReset.place(x=275,y=300)
entCustName.focus()
myForm.mainloop() #shows form and gives user interface control



