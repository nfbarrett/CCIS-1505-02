class Student (object):
    """HTC Student Class"""
    def __init__ (self, name=""): #constructor method
        print("HTC Student created!")
        self.StudentName = name.title() #create and attribute for student name
        print("Student Name: ", self.StudentName)

    def Greeting (self):
        print("Hello, I'm and HTC student!")

######MAINLINE######
strName = input("Enter student name: ")
objStudent = Student(name=strName) #creating and instance (object)[init]
objStudent.Greeting() #invokes greeting method
