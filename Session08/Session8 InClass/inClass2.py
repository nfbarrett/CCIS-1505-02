def Bday(name="",age=""): #function using keyword names and default values
    """comments here"""
    print (name, "you are", age, "years old!")

############ Mainline Code #############
strName = input("Enter name: ")
strAge = input("Enter age: ")

Bday(age=strAge, name=strName)
Bday(name=strName, age=strAge)


