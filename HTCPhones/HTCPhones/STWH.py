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
