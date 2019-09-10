# Programer: Nick Barrett
# Date Written: Sep 10, 2019
# Program Name: P3.py
# Company Name: HTC-CCIS1505

# step 2
str_first_name=input("Enter your first name in lower case: ")
print ("Raw input string is: " + str_first_name)

str_middle_name=input("Enter your middle name in lower case: ")
print ("Raw input string is: " + str_middle_name)

str_last_name=input("Enter your last name in lower case: ")
print ("Raw input string is: " + str_last_name)

str_full_name=(str_first_name + " " + str_middle_name + " " + str_last_name)
str_full_name=str_full_name.title()
print ("Input string in title is: " + str_full_name + "\n")

# step 3
int_age=int(input("Enter your age: "))
str_age = str(int_age * 2)

print ("Your age doubled is: " + str_age + "\n")

# step 4
print ("Addition")
int_number_1=int(input("Enter a number: "))
int_number_2=int(input("Enter another number: "))
str_number = str(int_number_1 + int_number_2)

print("The sum of these numbers is: " + str_number + "\n")

# step 5
print ("Subtraction")
int_number_1=int(input("Enter a number: "))
int_number_2=int(input("Enter another number: "))
str_number = str(int_number_1 - int_number_2)

print("The differance of these numbers is: " + str_number + "\n")

# step 6
print ("Multiplication")
int_number_1=int(input("Enter a number: "))
int_number_2=int(input("Enter another number: "))
str_number = str(int_number_1 * int_number_2)

print("The product of these numbers is: " + str_number + "\n")

# step 7
print ("Division")
int_number_1=int(input("Enter a number: "))
int_number_2=int(input("Enter another number: "))
str_number = '{:0.2f}'.format((int_number_1 / int_number_2))

print("The quotient of these numbers is: " + str_number + "\n")

# step 8
print ("Power of 10")
int_number_1=int(input("Enter a number: "))
str_number = str((int_number_1 ** 10))

print("The number raised to the power of 10 is: " + str_number + "\n")

# step 9
print ("Average")
int_number_1=int(input("Enter a number: "))
int_number_2=int(input("Enter another number: "))
int_number_3=int(input("Enter third number: "))
int_sum=(int_number_1 + int_number_2 + int_number_3)

str_number = '{:0.2f}'.format((int_sum / 3))

print("The quotient of these numbers is: " + str_number + "\n")

# step 10
print ("Temperature")
flt_number_1=float(input("Whats the temp: "))
flt_number=((flt_number_1 - 32) * (5/9))
str_number = '{:0.2f}'.format((flt_number))

print("Temperature in Celsius is: " + str_number + " degrees" + "\n")

