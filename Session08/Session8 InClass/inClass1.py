def Input():
    """This function get user's fn mn and ln and returs a string"""
    strFN = input("Enter your first name: ")
    strMN = input("Enter your middle name: ")
    strLN = input("Enter your last name: ")
    strFullName = strFN + " " + strMN + " " + strLN
    return strFullName
############ end of function

def Process(name):
    """This function receives a name and returns it in title format"""
    strFullNameT = name.title()
    return strFullNameT

def Output(name):
    """This function receives a name and prints a greeting message"""
    print ("Hello,", name, "have a nice day!")
    
    
######Mainline Code
strName = Input() #calls function and stores returned name in strName

strNameT = Process(strName)

Output(strNameT)






