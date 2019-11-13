class Student (object):
    """HTC Student Class"""
    GPA = 3.75  #class-level public attribute for GPA
    
    def __init__ (self, name="", ID=""): #constructor method
        print ("HTC Student created!")
        self.StudentName = name.title()  #create a public attribute for student name
        self.__StudentID = ID #create a private attribute for student ID (TechID)
        print ("Student Name:", self.StudentName)
        print ("Student ID:", self.__StudentID)
        print ("Student GPA:", self.GPA)
        
    def Greeting (self): 
        print ("Hello, I'm an HTC student!")

    def __str__(self):
        strPrint = "Student Name: " + self.StudentName + "   " + "Student ID:" + self.__StudentID
        return strPrint
    
    def __getID(self): #get method to RETURN private StudentID attribute
        strPW = input("Enter access code to retrieve StudentID: ")
        if strPW == "monkey":
            return self.__StudentID
        else:
            print ("Access code incorrect, access denied!")

    def __setID(self, ID=""):  #set method to MODIFY private StudentID attribute
        strPW = input("Enter access code to change StudentID: ")
        if strPW == "donkey":
            self.__StudentID = ID  #changes the private attribute value
        else:
            print ("Access code incorrect to change StudentID, access denied!")

    TechID = property(__getID, __setID)
#########Mainline##########
strName = input("Enter student name: ")
strID = input("Enter student ID: ")
objStudent = Student(name=strName, ID=strID)  #creating and instance (object)[instantiation]
print ()
#objStudent.Greeting()   #invokes Greeting method [obj.method]
print ()
##print (objStudent.StudentName)  #accessing the attribute StudentName  [obj.attr]
##print (objStudent.StudentID)    #accessing the attribute StudentID

#print (objStudent)
##print (objStudent.GPA) #access class-level variable
##objStudent.GPA = 4.0
##print (objStudent.GPA) #access class-level variable
##strID = objStudent.getID()
##print ("Student ID: ", strID)
##strID = input("Change StudentID to: ")
##
##objStudent.setID(ID=strID) #invoke set method to change StudentID
##
##strID = objStudent.getID()
##print ("Student ID: ", strID)
strID = objStudent.TechID  #use property to retrieve StudentID
print (strID)

strID = input("Change StudentID to: ")
objStudent.TechID = strID  #use property to change StudentID

strID = objStudent.TechID  #use property to retrieve StudentID
print (strID)










