def BV(l=1,w=1,h=1):
    """This functions receives 0,1,2 or 3 parameters and returns box volume"""
    try:
        intVol = int(l) * int(w) * int(h)
        return intVol
    except:
        return 0
####Mainline####
strL = input("Enter box length: ")
strW = input("Enter box width: ")
strH = input("Enter box height: ")

intBV = BV()  #no parameters passed in (use all defaults)
print ("Box volume is: ", intBV)

intBV = BV(l=strL)  #one parameter passed in (length)
print ("Box volume is: ", intBV)

intBV = BV(l=strL, w=strW)  #two parameters passed in (length & width)
print ("Box volume is: ", intBV)

intBV = BV(l=strL, w=strW, h=strH)  #thre parameters passed in (length & width & height)
print ("Box volume is: ", intBV)








