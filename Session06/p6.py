# Programer: Nick Barrett
# Date Written: Oct 01, 2019
# Program Name: P6.py
# Company Name: HTC-CCIS1505

#step 1
print("Step 1")

lstWeekDays = []
int_Counter=0
while int_Counter <= 6:
    strWeekDay = input("Enter day of the week: ")
    int_Counter += 1 # count up by 1
    strWeekDay = strWeekDay.title()
    lstWeekDays.append(strWeekDay)
print()
print()


#step 2
##lstWeekDays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
print("Step 2")

for lstWeek in lstWeekDays:
  print(lstWeek)
print()
print()


#step 3
print("Step 3")

##lstWeekDays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

lstWeekDays.reverse()

for lstRev in lstWeekDays:
  print(lstRev)
print()
print()


#step 4
print("Step 4")

##lstWeekDays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
lstWeekDays.sort()

for lstSort in lstWeekDays:
  print(lstSort)
print()
print()


#step 5
print("Step 5")

for strDay in lstWeekDays:
  print(strDay,"=",strDay[0:3])
print()
print()

#step 6
print("Step 6")

for strDay in lstWeekDays:
    if "T" in strDay[0]:
        print(strDay)


print()
print()


#step 7
print("Step 7")

dctCourses = {
    1000:"Intro to IS",
    1301:"HTML & CSS",
    1505:"Fundamentals of Programming",
    2575:".NET Programming 1",
    2585:".NET Programming 2",
    2701:"Database Design & SQL"}
print(dctCourses)
print()
print()


#step 8
print("Step 8")

lstKeys=dctCourses.keys()
for strKey in lstKeys:
        print(strKey)

print(lstKeys)
print()
print()


#step 9
print("Step 9")

lstValues=dctCourses.values()

for strValue in lstValues:
        print(strValue)
print()
print()


#step 10
print("Step 10")

strName = dctCourses[1505]
print(strName)
