blnDone = False # sets Boolean to false
while blnDone == False: # checks Boolean is still false
    try: # repeats this until Boolean is true
        num = int(input( "Enter your age" )) # asks for number, converts input into integer
        blnDone = True # sets Boolean to true
    except (ValueError): # if input is not a number will error out.
        print ("invalid age entered, please re-enter!") # returns error line and keeps Boolean to false and repeats
print ("Your age is", num) # once Boolean is true displays this line with the number
