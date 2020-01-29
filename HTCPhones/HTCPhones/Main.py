########HTC Phone Stores mainn Application  ###############

from STWH import *   #import Store/Warehouse classes
from tkinter import *  #import GUI TCL code
from STWHGUI import *  #import GUI class

objStore = Store()  #create Store object
objWhse = Warehouse()  #create whse object

myForm = Tk()  #create "root" form
myForm.geometry("800x500")  #size the form
myForm.title("HTC PHONE STORES")  #set form title bar
#myForm["bg"] = "royal blue"
myForm.configure(background="royal blue")

objGUI = STWHGUI(master=myForm,store=objStore,warehouse=objWhse)


myForm.mainloop() 
