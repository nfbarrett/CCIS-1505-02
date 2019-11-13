def maximumValue( x, y, z ): # calls the function for maximumvalue
    maximum = x # if position 1 is max this will be displayed 
    if y > maximum: # checks if position 2 is larger that position 1
        maximum = y # if position 2 is larger, position 2 will be displayed
    if z > maximum: # checks if position 3 is larger that position 1
        maximum = z # if position 3 is larger, position 3 will be displayed
    return maximum # displays the largest number

####Mainline#### # seperation of functions and the program

a = int(input( "Enter first integer: " ) ) # asks for 1st  number
b = int(input( "Enter second integer: " ) ) # asks for 2nd number
c = int(input( "Enter third integer: " ) ) # asks for 3rd number

print ("Maximum integer is:", maximumValue( a, b, c )) # calls function maximumValue and displays the result
