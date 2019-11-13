# Programer: Nick Barrett
# Date Written: Nov 5, 2019
# Program Name: P9.py
# Company Name: HTC-CCIS1505

class Employee:
    def __init__(self,strName,intHours,hourly_wage):
        self.Employee_Name = strName
        self.Hours_Worked = intHours
        self.Hourly_Wage = hourly_wage
        print ("PART 1 - Employee Name:", self.Employee_Name)
        print ("PART 1 - Employee Hours:", self.Hours_Worked)
        print ("PART 1 - Employee Wage: $", self.Hourly_Wage)

    @property
    def Empname(self):
        print("PART 2 - getter of Empname called")
        return self.Employee_Name

    @Empname.setter
    def setEmpname(self, emp_name):
        print("PART 2 - setter of Empname called")
        self.Employee_Name = emp_name

    def Emppay(self):
        if self.Hours_Worked <= 40:
            print("PART 3 - Employee Pay : $", round(self.Hours_Worked * self.Hourly_Wage,2))
        if self.Hours_Worked > 40:
            print ("PART 3 - Employee Pay : $",round(((self.Hours_Worked - 40) * (self.Hourly_Wage * 1.5)) + (self.Hourly_Wage * 40),2))



#########Mainline##########
print("PART 4")
strName = input("Employee Name: ")
intHours = int(input("Hours Worked: "))
hourly_wage = float(input("Hourly Wage: $")) 
myEmployee = Employee(strName,intHours,hourly_wage)
myEmployee.Emppay()


print()
print()
print("PART 5")
emp_name_change = input("What Employee name do you want to change? ")

if myEmployee.Employee_Name == emp_name_change:
    new_emp_name = input("Change {old_emp_name} to what new name? ".format(old_emp_name=emp_name_change))
    myEmployee.Employee_Name = new_emp_name
    print("{change_from}'s name changed to {change_to}".format(change_from=emp_name_change, change_to=new_emp_name))
else:
    print("No employee with name {change_from} exists. No names changed".format(change_from=emp_name_change))

print(myEmployee.Employee_Name)
