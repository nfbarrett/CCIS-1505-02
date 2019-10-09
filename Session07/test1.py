##sampleTuple=("ABC", "DEF", "HIJ", "KLM")
##
##print (sampleTuple)
##print (sampleTuple[1])
##print (sampleTuple[2:])
##print (sampleTuple[0:4])
##for element in sampleTuple:
##    print (element.lower())
##for element in sampleTuple:
##    print (element[0])
##print (len(sampleTuple))


firstName=input("enter your first name")
lastName=input("enter your last name")
if firstName == "":
 print ("you didn't enter a first name")
if lastName == "":
    print ("you didn't enter a last name")

    print ("Unable to process!")

else:

    fullName=firstName + lastName
    nameLen=len(fullName)
    print ("your name is " + str(nameLen) + " characters long")
    for letter in fullName:
        print (letter)
