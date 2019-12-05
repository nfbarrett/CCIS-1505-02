# Programer: Nick Barrett
# Date Written: Nov 12, 2019
# Program Name: P9.py
# Company Name: HTC-CCIS1505

class Employee:
    def __init__(self,strName="",intHours=0,hourly_wage=0.0): #constructor
        self.Employee_Name = strName #creat public Employee Name
        self.Hours_Worked = intHours #creat public Hours Worked
        self.__Hourly_Wage = hourly_wage #creat public Hourly Wage
        print ("Step 1 - Employee Name:", self.Employee_Name)
        print ("Step 1 - Employee Hours:", self.Hours_Worked)
        print ("Step 1 - Employee Wage: $", self.__Hourly_Wage)

    
    def getEmp(self):
        print("Step 2 - get Empname")
        return self.Employee_Name

    def setEmp(self, strNamechange):
        print("Step 2 - set Empname")
        self.Employee_Name = strNamechange

    Empname = property (getEmp,setEmp)

    def Emppay(self):
        if self.Hours_Worked <= 40:
            print("Step 3 - Employee Pay : $", round(self.Hours_Worked * self.__Hourly_Wage,2))
        if self.Hours_Worked > 40:
            print ("Step 3 - Employee 40+ hours Pay : $",round(((self.Hours_Worked - 40) * (self.__Hourly_Wage * 1.5)) + (self.__Hourly_Wage * 40),2))



#########Mainline##########
print("Step 4")
strName = input("Employee Name: ")
intHours = int(input("Hours Worked: "))
hourly_wage = float(input("Hourly Wage: $")) 
myEmployee = Employee(strName,intHours,hourly_wage)
myEmployee.Emppay()


print()
print()
print("Step 5")
strNamecheck = input("Change employee name to? ")
myEmployee.Empname=strNamecheck

##strNamechange = input("Change "+strNamecheck+" to what new name? ")
##print(myEmployee.Empname(strNamechange))

print(myEmployee.Employee_Name)
