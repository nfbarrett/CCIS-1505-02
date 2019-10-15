# Programer: Nick Barrett
# Date Written: Oct 15, 2019
# Program Name: L7.py
# Company Name: HTC-CCIS1505

def Input():
    """This function get users's fn and ln and returns a string"""
    strFN = input("Enter your first name: ")
    strMN = input("Enter your middle name: ")
    strLN = input("Enter your last name: ")
    strFullName = strFN + " " + strMN + " " + strLN
    return strFullName
#### end of function

def Process(name):
    """This function received a name and returns it in title format"""
    strFullNameT = name.title()
    return strFullNameT

def Output(name):
    """This function recives a name and prints a greating message"""
    print("Hello,", name, "have a nice day!")
    


######Mainline Code
strName= Input() #calls function and stores returned name in strName
print(strName)

strNameT = Process(strName)
print(strNameT)

Output(strNameT)
