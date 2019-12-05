#####HTC Phone Stores Application#########
class Store(object):
    def __init__(self, ID="", LOC="", items=0):  #constructor method
        self.ID = ID  #public attribute for store id
        self.Location = LOC #public attribute for store location (zipcode)
        self.__Inventory = int(items) #private attribute for store inventory
        print ()
        print ("Store ID:", self.ID, "created")
        print ("Store Location:", self.Location)
        print ("Store Inventory:", self.__Inventory)
        print()

    def __getInv(self):  #get method for Inventory
        return self.__Inventory
    def __setInv(self, items=0): #set method for Inventory
        self.__Inventory = int(items)
    inventory = property(__getInv, __setInv) #property to control access to private Inventory

    def Sale(self, items=0):  #conduct a Sale
        self.inventory -= int(items)
        print ("Phones being sold: ", items)
        
    def Return(self, items=0):  #conduct a Return
        self.inventory += int(items)
        print ("Phones being returned by customer: ", items)
        
    def Receive(self, items=0):  #conduct a Receive
        self.inventory += int(items)
        print ("Phones being received into inventory: ", items)
        
    def Xfer(self, items=0, whse=None):  #conduct a Transfer (store to whse)
        print ("Phones being transfered from store to whse: ", items)
        self.inventory -= int(items)
        whse.Receive(items=items)
    

class Warehouse(object):
    def __init__(self, ID="", LOC="", items=0):  #constructor method
        self.ID = ID  #public attribute for warehouse id
        self.Location = LOC #public attribute for warehouse location (zipcode)
        self.__Inventory = int(items) #private attribute for warehouse inventory
        print ()
        print ("Warehouse ID:", self.ID, "created")
        print ("Warehouse Location:", self.Location)
        print ("Warehouse Inventory:", self.__Inventory)
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
strID = input("Enter Store ID: ")
strLoc = input("Enter Store Location (zipcode): ")
strItems = input("Enter Store Inventory: ")

objStore = Store(ID=strID, LOC=strLoc, items=strItems)

strPhones = input("How many phones are being sold: ")
objStore.Sale(items=strPhones)
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














