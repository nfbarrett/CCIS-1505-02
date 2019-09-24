# Programer: Nick Barrett
# Date Written: Sep 24, 2019
# Program Name: L5.py
# Company Name: HTC-CCIS1505
##
##strName=input("Enter your name: ")
##for letter in strName:
##    print (letter)
##
##for intLC in range(100,-1,-10):
##    print(intLC)
##
##
##intLen = len(strName)
##print("You name has ", intLen, " characters in it!")
##
##
##strSearch = input("enter a character: ")
##
##
##if strSearch in strName: #membership (searching)
##    print("Your name has a(n)", strSearch,"in it")
##else:
##    print("Your name does not have a(n)", strSearch,"in it")
##print(strName[3])

tupStudents = ("bob", "joe", "tom", "tim", "sue", "jim", "ann")

print(tupStudents)
print()

for student in tupStudents:
    print(student.title())
print()
tupLen = len(tupStudents)
print("there are",tupLen, "students in the class")
