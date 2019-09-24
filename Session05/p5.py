# Programer: Nick Barrett
# Date Written: Sep 24, 2019
# Program Name: P5.py
# Company Name: HTC-CCIS1505

#step 1
strFirstName=input("Enter your first name: ")
strLastName=input("Enter your last name: ")
intLenFirst = len(strFirstName)
intLenLast = len(strLastName)

print("You first name has", intLenFirst, "characters in it and your last name has",intLenLast,"in it!")

#step 2

tupMonthNames = ("January","Febuary","March","April","May","June","July","August","September","October","November","December")

print(tupMonthNames)

#step 3

for x in tupMonthNames:
  print(x) 


#step 4
if "J" in tupMonthNames:
    print("Yes")






#step 5

strSearchMonth = input("Enter a Month: ")

if strSearchMonth in tupMonthNames:
    print("Month found!")
else:
    print("Month not found")
#step 6


#step 7
