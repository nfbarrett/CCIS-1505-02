def GetNames():
    """This function collects names from keyboard and returns a list of names"""
    lstNames = []
    blnDone = False
    while blnDone == False:
        strName = input("Enter a name or press ENTER when done: ")
        if len(strName) > 0:  #Did user enter a name
            lstNames.append(strName.title())
        else:  #user pressed ENTER
            blnDone=True
    return lstNames

#########Mainline Code##########
lstData = GetNames()
lstData.sort()
print (lstData)
