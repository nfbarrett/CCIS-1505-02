########HTC Phone Stores GUI Class ###########
from tkinter import *
class STWHGUI(object):
    ############# Default colors & fonts ################
    bg = "royal blue"
    fg = "sky blue"
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
    ###Store Xacts
    def SSale (self):
        strItems = self.entItems.get()
        self.store.Sale(items=strItems)
        self.lblSInv["text"] = self.store.inventory

    def SReturn (self):
        strItems = self.entItems.get()
        self.store.Return(items=strItems)
        self.lblSInv["text"] = self.store.inventory

    def SReceive (self):
        strItems = self.entItems.get()
        self.store.Receive(items=strItems)
        self.lblSInv["text"] = self.store.inventory

    def SXfer (self):
        strItems = self.entItems.get()
        self.store.Xfer(items=strItems,whse=self.warehouse)
        self.lblSInv["text"] = self.store.inventory
        self.lblWInv["text"] = self.warehouse.inventory

    ###Whse Xacts
    def WShip (self):
        strItems = self.entItems.get()
        self.warehouse.Ship(items=strItems)
        self.lblWInv["text"] = self.warehouse.inventory

    def WReturn (self):
        strItems = self.entItems.get()
        self.warehouse.Return(items=strItems)
        self.lblWInv["text"] = self.warehouse.inventory

    def WReceive (self):
        strItems = self.entItems.get()
        self.warehouse.Receive(items=strItems)
        self.lblWInv["text"] = self.warehouse.inventory

    def WXfer (self):
        strItems = self.entItems.get()
        self.warehouse.Xfer(items=strItems,store=self.store)
        self.lblSInv["text"] = self.store.inventory
        self.lblWInv["text"] = self.warehouse.inventory

    def __init__(self,master=None,store=None,warehouse=None):
        self.master = master
        self.store = store
        self.warehouse = warehouse
        self.ControlsOnForm()

    def ControlsOnForm(self):
        self.lblLogo = Label(text="HTC PHONE STORES",fg=self.fg,bg=self.bg,font=self.f1)
        self.lblLogo.place(x=260,y=10)
        self.lblItems = Label(text="Items:",fg=self.fg,bg=self.bg,font=self.f2)
        self.lblItems.place(x=275,y=60)
        self.entItems = Entry(fg=self.bg,bg="white",font=self.f2,width=8)
        self.entItems.place(x=375,y=60)
        self.lblSxacts = Label(text="Store Transactions",fg=self.fg,bg=self.bg,font=self.f2)
        self.lblSxacts.place(x=150,y=100)
        self.lblWxacts = Label(text="Warehouse Transactions",fg=self.fg,bg=self.bg,font=self.f2)
        self.lblWxacts.place(x=425,y=100)

        ########## Store Buttons #########
        self.btnSSale = Button(text="Sale",fg="gold",bg=self.bg,font=self.f3,width=10,command=self.SSale)
        self.btnSSale.place(x=180,y=150)
        self.btnSRtn = Button(text="Return",fg="gold",bg=self.bg,font=self.f3,width=10,command=self.SReturn)
        self.btnSRtn.place(x=180,y=200)
        self.btnSRcv = Button(text="Receive",fg="gold",bg=self.bg,font=self.f3,width=10,command=self.SReceive)
        self.btnSRcv.place(x=180,y=250)
        self.btnSXfer = Button(text="Transfer",fg="gold",bg=self.bg,font=self.f3,width=10,command=self.SXfer)
        self.btnSXfer.place(x=180,y=300)
        ########## Warehouse Buttons #########
        self.btnWShip = Button(text="Ship",fg="gold",bg=self.bg,font=self.f3,width=10,command=self.WShip)
        self.btnWShip.place(x=500,y=150)
        self.btnWRtn = Button(text="Return",fg="gold",bg=self.bg,font=self.f3,width=10,command=self.WReturn)
        self.btnWRtn.place(x=500,y=200)
        self.btnWRcv = Button(text="Receive",fg="gold",bg=self.bg,font=self.f3,width=10,command=self.WReceive)
        self.btnWRcv.place(x=500,y=250)
        self.btnWXfer = Button(text="Transfer",fg="gold",bg=self.bg,font=self.f3,width=10,command=self.WXfer)
        self.btnWXfer.place(x=500,y=300)
        ###################################################################################
        self.lblSInventory = Label(text="Inventory:",bg=self.bg,fg=self.fg,font=self.f2)
        self.lblSInventory.place(x=160,y=350)
        self.lblSInv = Label(text="000",fg=self.fg,bg=self.bg,font=self.f2)
        self.lblSInv.place(x=285,y=350)
        self.lblWInventory = Label(text="Inventory:",bg=self.bg,fg=self.fg,font=self.f2)
        self.lblWInventory.place(x=480,y=350)
        self.lblWInv = Label(text="000",fg=self.fg,bg=self.bg,font=self.f2)
        self.lblWInv.place(x=605,y=350)
        ########## Action Buttons  #########
        self.btnReset = Button(text="Reset",fg="gold",bg=self.bg,font=self.f2,width=10,command=self.Reset)
        self.btnReset.place(x=500,y=425)
        self.btnClose = Button(text="Close",fg="red",bg=self.bg,font=self.f2,width=10,command=self.Close)
        self.btnClose.place(x=642,y=425)

        self.entItems.focus()
