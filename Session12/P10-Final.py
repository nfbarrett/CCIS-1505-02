# Programer: Nick Barrett
# Date Written: Dec 17, 2019
# Program Name: P10-Final.py
# Company Name: HTC-CCIS1505

########ATM interface Application  ###############

from P10A import *   #import Store/Warehouse classes
from tkinter import *  #import GUI TCL code
from P10GUI import *  #import GUI class

objChecking = Checking()  #create Store object
objSavings = Savings()  #create whse object

myForm = Tk()  #create "root" form
myForm.geometry("800x500")  #size the form
myForm.title("Nick's ATM")  #set form title bar
#myForm["bg"] = "royal blue"
myForm.configure(background="green")

objGUI = P10GUI(master=myForm,checking=objChecking,savings=objSavings)


myForm.mainloop()
