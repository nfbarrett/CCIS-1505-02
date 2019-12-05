# Programer: Nick Barrett
# Date Written: Dec 3, 2019
# Program Name: P10.py
# Company Name: HTC-CCIS1505

#####HTC Phone Stores Application#########
class Checking(object):
    def __init__(self, ID="", Own="", balance=0):  #constructor method
        self.ID = ID  #public attribute for Checking id
        self.Own = Own #public attribute for Checking name
        self.__Balance = int(balance) #private attribute for Checking balance
        print ()
        print ("Savings ID:", self.ID, "created")
        print ("Owner:", self.Own)
        print ("Warehouse Inventory:", self.__Balance)
        print()

    def __getInv(self):  #get method for Inventory
        return self.__Inventory
    def __setInv(self, balance=0): #set method for Inventory
        self.__Inventory = int(balance)
    inventory = property(__getInv, __setInv) #property to control access to private Inventory

    def Sale(self, balance=0):  #conduct a Sale
        self.inventory -= int(balance)
        print ("Phones being sold: ", balance)
        
    def Return(self, balance=0):  #conduct a Return
        self.inventory += int(items)
        print ("Phones being returned by customer: ", balance)
        
    def Receive(self, balance=0):  #conduct a Receive
        self.inventory += int(items)
        print ("Phones being received into inventory: ", balance)
        
    def Xfer(self, balance=0, whse=None):  #conduct a Transfer (store to whse)
        print ("Phones being transfered from store to whse: ", balance)
        self.inventory -= int(balance)
        whse.Receive(balance=balance)
    

class Savings(object):
    def __init__(self, ID="", Own="", balance=0):  #constructor method
        self.ID = ID  #public attribute for Savings id
        self.Own = Own #public attribute for Savings name
        self.__Balance = int(balance) #private attribute for Savings balance
        print ()
        print ("Savings ID:", self.ID, "created")
        print ("Owner:", self.Own)
        print ("Warehouse Inventory:", self.__Balance)
        print()

    def __getInv(self):  #get method for Inventory
        return self.__Inventory
    def __setInv(self, items=0): #set method for Inventory
        self.__Inventory = int(items)
    inventory = property(__getInv, __setInv) #property to control access to private Inventory

    def Ship(self, items=0):  #conduct a Ship
        self.inventory -= int(items)
        print ("Phones being shipped to store: ", items)
        
    def Return(self, items=0):  #conduct a Return
        self.inventory -= int(items)
        print ("Phones being returned by customer: ", items)
        
    def Receive(self, items=0):  #conduct a Receive
        self.inventory += int(items)
        print ("Phones being received into inventory: ", items)
        
    def Xfer(self, items=0, store=None):  #conduct a Transfer (whse to store)
        print ("Phones being whse to store: ", items)
        self.inventory -= int(items)
        store.Receive(items=items)


######Mainline#######

#######Create Store Object and conduct transactions        
accID = input("Enter Account #: ")
accOwn = input("Enter Account Name: ")
accBalance = input("Enter Starting Balance: ")

objChecking = Checking(ID=accID, Own=accOwn, balance=accBalance)

strPhones = input("How many phones are being sold: ")
objChecking.Sale(balance=strPhones)
print ("Store Inventory: ",objStore.inventory)

strPhones = input("How many phones are being returned by customer: ")
objStore.Return(items=strPhones)
print ("Store Inventory: ",objStore.inventory)

strPhones = input("How many phones are being receive into inventory: ")
objStore.Receive(items=strPhones)
print ("Store Inventory: ",objStore.inventory)

#########################################################
#######Create Warehouse Object and conduct transactions
strID = input("Enter Warehouse ID: ")
strLoc = input("Enter  Warehouse (zipcode): ")
strItems = input("Enter Warehouse Inventory: ")

objWhse = Warehouse(ID=strID, LOC=strLoc, items=strItems)

strPhones = input("How many phones are being shipped to store: ")
objWhse.Ship(items=strPhones)
print ("Warehouse Inventory: ",objWhse.inventory)

strPhones = input("How many phones are being returned to vendor: ")
objWhse.Return(items=strPhones)
print ("Warehouse Inventory: ",objWhse.inventory)

strPhones = input("How many phones are being received into inventory: ")
objWhse.Receive(items=strPhones)
print ("Warehouse Inventory: ",objWhse.inventory)


######Transfers
strPhones = input("How many phones are being transfered from store to whse: ")
objStore.Xfer(items=strPhones, whse=objWhse)
print ("Store Inventory: ",objStore.inventory)
print ("Warehouse Inventory: ",objWhse.inventory)

strPhones = input("How many phones are being transfered from whse to store: ")
objWhse.Xfer(items=strPhones, store=objStore)
print ("Store Inventory: ",objStore.inventory)
print ("Warehouse Inventory: ",objWhse.inventory)

















#Step 1
#Have the user open a savings account and a checking account by entering a beginning balance for each account.

#intCheck = input("Enter amount to depoist in Checking: $")
#intSave = input("Enter amount to depoist in Saving: $")

#objChecking = Checking(intCheck) #creating and instance (object)[init]
#objSaving = Saving(intSave) #creating and instance (object)[init]

#Print the balance of each account.


#Step 2
#Ask the user for an amount to deposit into the savings account, then add it to the balance for the savings account.

#intSave = input("Enter amount to depoist in Saving: $")
#objSaving = Saving(depositAmount(intSave)) #creating and instance (object)[init]


#Print the balance.


#Step 3
#Ask the user for an amount to deposit into the checking account then add it to the balance for the checking account.

#Print the balance.


#Step 4
#Ask the user for an amount to withdraw from the savings account then subtract that amount from the balance for the savings account.

#Print the balance.


#Step 5
#Ask the user for an amount to withdraw from the checking account then subtract that amount from the balance for the checking account.

#Print the balance.


#Step 6
#Ask the user to input the dollar amount to transfer from the checking account to the savings account.

#Print the balance of both the checking and savings accounts.


#Step 7
#Ask the user to input the dollar amount to transfer from the savings account to the checking account.

#Print the balance of both the checking and savings accounts.
