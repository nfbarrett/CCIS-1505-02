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
    def __setInv(self, items=0.00): #set method for Inventory
        self.__Inventory = int(items)
    inventory = property(__getInv, __setInv) #property to control access to private Inventory

    def Spent(self, items=0.00):  #conduct a Sale
        self.inventory -= int(items)
        print ("Checking spent: ", items)

    def Deposite(self, items=0.00):  #conduct a deposited
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

print("Step 1")
#Have the user open a savings account and a checking account by entering a beginning balance for each account.

intCheck = input("Enter amount to depoist in Checking: $")
objChecking = Checking("C-1983","MN",intCheck) #creating and instance (object)[init]
objSavings = Savings("C-1983","MN",0) #creating and instance (object)[init]

#Print the balance of each account.
print ("Balance: ")
print ("Checking: ",objChecking.inventory)
print ("Savings: ",objSavings.inventory)

print()
print("Step 2")
#Ask the user for an amount to deposit into the savings account, then add it to the balance for the savings account.

depSavings = input("Enter amount to depoist in Saving: $")

#Print the balance.
objSavings.Deposite(items=depSavings) #creating and instance (object)[init]
print()

print("Step 3")
#Ask the user for an amount to deposit into the checking account then add it to the balance for the checking account.
depCheck = input("Enter amount to depoist in Checking: $")
objChecking.Deposite(items=depCheck)

#Print the balance of each account.
print ("Balance: ")
print ("Checking: ",objChecking.inventory)
print ("Savings: ",objSavings.inventory)


print()
print("Step 4")
#Ask the user for an amount to withdraw from the savings account then subtract that amount from the balance for the savings account.
witSave = input("Enter amount to withdraw from Saving: $")
objSavings.Spent(items=witSave)


#Print the balance.
print ("Balance: ")
print ("Savings: ",objSavings.inventory)

print()
print("Step 5")
#Ask the user for an amount to withdraw from the checking account then subtract that amount from the balance for the checking account.
witCheck = input("Enter amount to withdraw from Checking: $")
objChecking.Spent(items=witCheck)


#Print the balance.
print ("Balance: ")
print ("Checking: ",objChecking.inventory)


print()
print("Step 6")
#Ask the user to input the dollar amount to transfer from the checking account to the savings account.
transCheck = input("Enter amount to transfer from Checking to Saving: $")
objChecking.Xfer(items=transCheck,savings=objSavings)



#Print the balance of both the checking and savings accounts.
print ("Balance: ")
print ("Checking: ",objChecking.inventory)
print ("Savings: ",objSavings.inventory)

print()
print("Step 7")
#Ask the user to input the dollar amount to transfer from the savings account to the checking account.
transSaving = input("Enter amount to transfer from Checking to Saving: $")
objSavings.Xfer(items=transSaving,checking=objChecking)

#Print the balance of both the checking and savings accounts.
print ("Balance: ")
print ("Checking: ",objChecking.inventory)
print ("Savings: ",objSavings.inventory)
