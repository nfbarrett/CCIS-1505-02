# Programer: Nick Barrett
# Date Written: Sep 17, 2019
# Program Name: P4.py
# Company Name: HTC-CCIS1505


# step 2
print("\nstep 2 1 to 10 by 1")
int_Counter = 1
while int_Counter <= 10:
    print("Loop Counter is: ", int_Counter)
    int_Counter += 1 # count up by 1

# step 3
print("\nstep 3 1 to 101 by 10")
int_Counter = 1
while int_Counter <= 101:
    print("Loop Counter is: ", int_Counter)
    int_Counter += 10 # count up by 10

# step 4
print("\nstep 4 1000 down to 0 by 100")
int_Counter = 1000
while int_Counter >= 0:
    print("Loop Counter is: ", int_Counter)
    int_Counter -= 100 # count down by 100

# step 5
print("\nstep 5 IF")
int_number = int(input("Pick a number between 1 - 10: "))
if int_number == 1:
    print("One")
elif int_number == 2:
    print("Two")
elif int_number == 3:
    print("Three")
elif int_number == 4:
    print("Four")
elif int_number == 5:
    print("Five")
elif int_number == 6:
    print("Six")
elif int_number == 7:
    print("Seven")
elif int_number == 8:
    print("Eight")
elif int_number == 9:
    print("Nine")
elif int_number == 10:
    print("Ten")
else:
    print("Sorry, you choose a number outside of 1 - 10.")


# step 6
print("\nstep 6 LOGIN")

blnDone = False
while blnDone == False:
    str_name = input("Username: ")
    str_pass = input("Password: ")
    if str_name == "john doe" and str_pass == "fopwpo":
        print("Login successful\n")
        blnDone = True
    else:
        print("Login unsuccessful\n")



