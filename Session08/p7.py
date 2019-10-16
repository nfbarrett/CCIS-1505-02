# Programer: Nick Barrett
# Date Written: Oct 15, 2019
# Program Name: P7.py
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


#step 1
print("Step 1")
strName= Input() #calls function and stores returned name in strName
print(strName)

strNameT = Process(strName)
print(strNameT)

Output(strNameT)
print()
print()
#step 2
print("Step 2")

print()
print()
#step 3
print("Step 3")

print()
print()
#step 4
print("Step 4")

print()
print()
#step 5
print("Step 5")

print()
print()
#step 6
print("Step 6")

print()
print()
# step 7
print("Step 7")

print()
print()
#step 8
print("Step 8")

print()
print()
#step 9
print("Step 9")

print()
print()
#step 10
print("Step 10")

