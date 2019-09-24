# Programer: Nick Barrett
# Date Written: Sep 24, 2019
# Program Name: P5.py
# Company Name: HTC-CCIS1505

#step 1
print("Step 1")
strFirstName=input("Enter your first name: ")
strLastName=input("Enter your last name: ")
intLenFirst = len(strFirstName)
intLenLast = len(strLastName)

print("You first name has", intLenFirst, "characters in it and your last name has",intLenLast,"in it!")
print()

#step 2
print("Step 2")
tupMonthNames = ("January","Febuary","March","April","May","June","July","August","September","October","November","December")

print(tupMonthNames)
print()

#step 3
print("Step 3")
for tupMon in tupMonthNames:
  print(tupMon,"=",tupMon[0:3]) 
print()

#step 4
print("Step 4")
for tupMon in tupMonthNames:
    if "J" in tupMon[0]:
        print(tupMon)

print()

#step 5
print("Step 5")
strSearchMonth = input("Enter a Month: ")

if strSearchMonth.title() in tupMonthNames:
    print("Month found!")
else:
    print("Month not found")
print()
#step 6
print("Step 6")
strFirstName=input("Enter your first name: ")
for intLC in range(1,11,1):
    print(strFirstName, "loop counter =", intLC)

print()
#step 7
print("Step 7")
for intLC2 in range(1,20,2):
    print (intLC2)
