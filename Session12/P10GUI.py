# Programer: Nick Barrett
# Date Written: Dec 17, 2019
# Program Name: P10GUI.py
# Company Name: HTC-CCIS1505

########ATM GUI###########
from tkinter import *
class P10GUI(object):
    ############# Default colors & fonts ################
    bg = "green"
    fg = "light green"
    btntxt = "light green"
    f1 = "Arial 16 bold"
    f2 = "Arial 14 bold"
    f3 = "Arial 14"
    #####################################################

    ########### Event Procedures ###################
    def Reset(self):
        self.entItems.delete(0,END)
        self.entItems.focus()

    def Close(self):
        self.master.destroy()
    ###Checking Xacts
    def CSpent (self):
        strItems = self.entItems.get()
        self.checking.Spent(items=strItems)
        self.lblCInv["text"] = self.checking.inventory

    def CDeposite (self):
        strItems = self.entItems.get()
        self.checking.Deposite(items=strItems)
        self.lblCInv["text"] = self.checking.inventory

    def CXfer (self):
        strItems = self.entItems.get()
        self.checking.Xfer(items=strItems,savings=self.savings)
        self.lblCInv["text"] = self.checking.inventory
        self.lblSInv["text"] = self.savings.inventory

    ###Whse Xacts
    def SSpent (self):
        strItems = self.entItems.get()
        self.savings.Spent(items=strItems)
        self.lblSInv["text"] = self.savings.inventory

    def SDeposite (self):
        strItems = self.entItems.get()
        self.savings.Deposite(items=strItems)
        self.lblSInv["text"] = self.savings.inventory

    def SXfer (self):
        strItems = self.entItems.get()
        self.savings.Xfer(items=strItems,checking=self.checking)
        self.lblCInv["text"] = self.checking.inventory
        self.lblSInv["text"] = self.savings.inventory

    def __init__(self,master=None,checking=None,savings=None):
        self.master = master
        self.checking = checking
        self.savings = savings
        self.ControlsOnForm()

    def ControlsOnForm(self):
        self.lblLogo = Label(text="Nick's ATM",fg=self.fg,bg=self.bg,font=self.f1)
        self.lblLogo.place(x=260,y=10)
        self.lblItems = Label(text="Amount:",fg=self.fg,bg=self.bg,font=self.f2)
        self.lblItems.place(x=275,y=60)
        self.entItems = Entry(fg=self.bg,bg="white",font=self.f2,width=8)
        self.entItems.place(x=375,y=60)
        self.lblCxacts = Label(text="Checking Transactions",fg=self.fg,bg=self.bg,font=self.f2)
        self.lblCxacts.place(x=150,y=100)
        self.lblSxacts = Label(text="Savings Transactions",fg=self.fg,bg=self.bg,font=self.f2)
        self.lblSxacts.place(x=425,y=100)

        ########## Checking Buttons #########
        self.btnCSpent = Button(text="Withdraw",fg=self.btntxt,bg=self.bg,font=self.f3,width=10,command=self.CSpent)
        self.btnCSpent.place(x=180,y=150)
        self.btnCDeposite = Button(text="Deposite",fg=self.btntxt,bg=self.bg,font=self.f3,width=10,command=self.CDeposite)
        self.btnCDeposite.place(x=180,y=250)
        self.btnCXfer = Button(text="Transfer",fg=self.btntxt,bg=self.bg,font=self.f3,width=10,command=self.CXfer)
        self.btnCXfer.place(x=180,y=300)
        ########## Savings Buttons #########
        self.btnSSpent = Button(text="Withdraw",fg=self.btntxt,bg=self.bg,font=self.f3,width=10,command=self.SSpent)
        self.btnSSpent.place(x=500,y=150)
        self.btnSDeposite = Button(text="Deposite",fg=self.btntxt,bg=self.bg,font=self.f3,width=10,command=self.SDeposite)
        self.btnSDeposite.place(x=500,y=250)
        self.btnSXfer = Button(text="Transfer",fg=self.btntxt,bg=self.bg,font=self.f3,width=10,command=self.SXfer)
        self.btnSXfer.place(x=500,y=300)
        ###################################################################################
        self.lblCInventory = Label(text="Balance:",bg=self.bg,fg=self.fg,font=self.f2)
        self.lblCInventory.place(x=160,y=350)
        self.lblCInv = Label(text="$0.00",fg=self.fg,bg=self.bg,font=self.f2)
        self.lblCInv.place(x=285,y=350)
        self.lblSInventory = Label(text="Balance:",bg=self.bg,fg=self.fg,font=self.f2)
        self.lblSInventory.place(x=480,y=350)
        self.lblSInv = Label(text="$0.00",fg=self.fg,bg=self.bg,font=self.f2)
        self.lblSInv.place(x=605,y=350)
        ########## Action Buttons  #########
        self.btnReset = Button(text="Reset",fg=self.btntxt,bg=self.bg,font=self.f2,width=10,command=self.Reset)
        self.btnReset.place(x=500,y=425)
        self.btnClose = Button(text="Close",fg="black",bg="red",font=self.f2,width=10,command=self.Close)
        self.btnClose.place(x=642,y=425)

        self.entItems.focus()
