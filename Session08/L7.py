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

strName= Input()
print(strName)
