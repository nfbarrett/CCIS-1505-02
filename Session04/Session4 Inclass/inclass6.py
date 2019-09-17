blnDone = False
while blnDone == False:

    print \
    ("""
    Welcome to STEVE's Cafe, here is the menu:
    1) eggs & toast
    2) oatmeal
    3) omlette
    4) french toast
    5) wheaties
    """)
    strChoice = input("Enter your choice: ")
    if strChoice == "1":
        print ("Enjoy your eggs & toast!")
        blnDone = True
    elif strChoice == "2":
        print ("Enjoy your oatmeal!")
        blnDone = True
    elif strChoice == "3":
        print ("Enjoy your omlette!")
        blnDone = True 
    elif strChoice == "4":
        print ("Enjoy your french toast!")
        blnDone = True
    elif strChoice == "5":
        print ("Enjoy your wheaties!")
        blnDone = True
    else:
        print ("You didn't choose a valid menu item")
        print ("Please choose again!")









    
