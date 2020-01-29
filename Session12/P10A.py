# Programer: Nick Barrett
# Date Written: Dec 3, 2019
# Program Name: P10.py
# Company Name: HTC-CCIS1505


class Checking(object):
    def __init__(self, ID="C-1983", LOC="MN", items=0.00):  #constructor method
        self.ID = ID  #public attribute for Checking id
        self.Location = LOC #public attribute for Checking location (zipcode)
        self.__Inventory = int(items) #private attribute for Checking inventory
        print ()
        print ("Checking ID:", self.ID, "created")
        print ("Checking Location:", self.Location)
        print ("Checking Inventory:", self.__Inventory)
        print()

    def __getInv(self):  #get method for Inventory
        return self.__Inventory
    def __setInv(self, items=0): #set method for Inventory
        self.__Inventory = int(items)
    inventory = property(__getInv, __setInv) #property to control access to private Inventory

    def Spent(self, items=0):  #conduct a Sale
        self.inventory -= int(items)
        print ("Checking spent: ", items)

    def Deposite(self, items=0):  #conduct a deposited
        self.inventory += int(items)
        print ("Checking deposited: ", items)

    def Xfer(self, items=0, savings=None):  #conduct a Transfer (Checking to Savings)
        print ("Transfered from Checking to Savings: ", items)
        self.inventory -= int(items)
        savings.Deposite(items=items)

class Savings(object):
    def __init__(self, ID="S-1983", LOC="MN", items=0.00):  #constructor method
        self.ID = ID  #public attribute for Savings id
        self.Location = LOC #public attribute for Savings location (zipcode)
        self.__Inventory = int(items) #private attribute for Savings inventory
        print ()
        print ("Savings ID:", self.ID, "created")
        print ("Savings Location:", self.Location)
        print ("Savings Inventory:", self.__Inventory)
        print()

    def __getInv(self):  #get method for Inventory
        return self.__Inventory
    def __setInv(self, items=0): #set method for Inventory
        self.__Inventory = int(items)
    inventory = property(__getInv, __setInv) #property to control access to private Inventory

    def Spent(self, items=0):  #conduct a Spent
        self.inventory -= int(items)
        print ("Spent from Savings: ", items)

    def Deposite(self, items=0):  #conduct a Deposite
        self.inventory += int(items)
        print ("Deposited into Savings: ", items)

    def Xfer(self, items=0, checking=None):  #conduct a Transfer (Savings to Checking)
        print ("Transfered from Savings to Checking: ", items)
        self.inventory -= int(items)
        checking.Deposite(items=items)



