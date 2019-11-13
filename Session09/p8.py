# Programer: Nick Barrett
# Date Written: Oct 22, 2019
# Program Name: P8.py
# Company Name: HTC-CCIS1505


def GetNames():
    """This function collects scores from keyboard and returns a list of names"""
    lstNames = []
    blnDone = False
    while blnDone == False:
        strNames = input("Enter a Name or press ENTER when done: ")
        if len(strNames) > 0:  #Did user enter a name
            lstNames.append(strNames)
        else:  #user pressed ENTER
            blnDone=True
    return lstNames


print("Part 1")
GetNames()


filNames = open(file="NAMES.txt",mode="a")  #open file for appending
filNames.writelines(lstNames)  #write lines to (LSV) file
filNames.close() #close file
print (lstNames)


filNames = open(file="NAMES.txt",mode="r")  #open file for reading
lstNames = filNames.readlines() #read lines into list (LSV file)
filNames.close() #close file

lstNames.sort()

print (lstNames)
