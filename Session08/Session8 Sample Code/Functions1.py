#Sample Program Using Functions


#Define functions
def DataEntry():
    """ This function asks the user for their first name,
        then asks for their last name
        then concatenates the first name, a space, and then the last name"""
    firstName=input("Enter your first name in lower case: ")
    lastName=input("Enter your last name in lower case: ")
    fullName= firstName + " " + lastName
    return fullName

def DataConversion(namePassedIn):
    nameTitleFmt=namePassedIn.title()
    return nameTitleFmt

def DataPrint(formattedName):
    print ("Hello, " + formattedName + ".  Have a nice day!")


######Mainline Code
userName=DataEntry()  #call function to get name (input)
userNameTitle=DataConversion(userName)  #call function to format name (process)
DataPrint(userNameTitle)  #call function to print formatted name (output)
