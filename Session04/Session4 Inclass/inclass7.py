blnDone = False
while blnDone == False:
    strGuess = input("enter a number between 1 and 10: ")
    if strGuess == "7" or strGuess == "9": #compound using or
        print ("You guessed correct!")
        blnDone = True
