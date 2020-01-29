# Programer: Nick Barrett
# Date Written: Dec 17, 2019
# Program Name: Final.py
# Company Name: HTC-CCIS1505


class Employee:
    def __init__(self,strName="",intHours=0,hourly_wage=0.0): #constructor
        self.Employee_Name = strName #creat public Employee Name
        self.Hours_Worked = int(intHours) #creat public Hours Worked
        self.__Hourly_Wage = float(hourly_wage) #creat public Hourly Wage

    def __getPay(self):  #get method for pay
        return self.__pay
    def __setPay(self, pay=0.00): #set method for pay
        self.__pay = int(items)
    pay = property(__getPay, __setPay) #property to control access to private pay

    def Payroll():
            filEmployee = []
            blnDone = False
            while blnDone == False:
                strName = input("Employee Name: ")
                intHours = int(input("Hours Worked: "))
                hourly_wage = float(input("Hourly Wage: $"))
                if strName == "DONE":
                    filEmployee = open(file="Employee.txt",mode="r")
                    lstEmployee = filEmployee.readlines()
                    filEmployee.close() #close file
                    Employee.Emppay(lstEmployee[0],lstEmployee[1],lstEmployee[2])
                    blnDone = True
                else:
                    tup1  = strName + "," + intHours + "," + hourly_wage
                    filEmployee = open(file="Employee.txt",mode="a")
                    myEmployee = filEmployee.write(tup1 + "\n")
                    filEmployee.close() #close file
                    print()

       
    def getEmp(self):
        print("Get Employee Name")
        return self.Employee_Name

    def setEmp(self, strNamechange):
        print("Set Employee Name")
        self.Employee_Name = strNamechange

    Empname = property (getEmp,setEmp)

    def Emppay(self,strName,Hours_Worked,__Hourly_Wage):
        
        if self.Hours_Worked <= 40:
            print("Employee Pay : $", round(self.Hours_Worked * self.__Hourly_Wage,2))
        if self.Hours_Worked > 40:
            print ("Employee 40+ hours Pay : $",round(((self.Hours_Worked - 40) * (self.__Hourly_Wage * 1.5)) + (self.__Hourly_Wage * 40),2))

    

#########Mainline##########
objEmployee = Employee.Payroll();



print(objEmployee)
