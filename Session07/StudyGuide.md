# FOP/WPO Exam #1 Study Guide

1. Syntax is the rules that you must follow when coding programs.

- [ ] True
- [ ] False

2. Strings, integers, floating point and boolean are four of the simple data types used in computers.

- [ ] True
- [ ] False

3. Syntax errors must be corrected before your program will execute.

- [ ] True
- [ ] False

4. A variable is a data element that is created in secondary storage.

- [ ] True
- [ ] False

5. Two basic approaches used to design program logic include using flowhcharts and pseudocode.

- [ ] True
- [ ] False

6. A runtime error typically means that your program “crashes” with a fatal error.

- [ ] True
- [ ] False

7. It is a good practice to compare data with different types.

- [ ] True
- [ ] False

8. Structured programming provides only one entry point and one exit point for a logic structure.

- [ ] True
- [ ] False

9. Concatenation and addition are operations that basically do the same thing because they both use the "+" sign for the operator.

- [ ] True
- [ ] False

10. Placing comments in a computer program make it less efficient and waste time and money.

- [ ] True
- [ ] False

11. Which function is not used to convert data types and values:
  - int
  - input
  - str
  - float


12. Which of the following is not a valid relational operator:
  - =
  - >
  - <
  - ==

13. A loop that uses a counter requires:
  - initialize counter, test for completion, break
  - continue, return, break
  - initialize counter, test for completion, process block, increment counter
  - process block, return


14. A string can be described as a(n):
  - instruction
  - integer
  - float
  - sequence


15. If A is a string, and B is a string, then the statement C=A+B would:
  - add A and B
  - set B equal to C
  - create a new string C by concatenating A and B
  - set A equal to B


16. If A is a string that contains value “PYTHON”, what would A[2:4] represent:
  - "A24"
  - "PY"
  - "TH"
  - "YT"

17. A tuple can best be described as:
  - function
  - string
  - sequence
  - number

19. A type error means that the programmer has:
  - made a typing mistake
  - programmed a syntax error
  - mixed data types in an operation
  - mixed upper and lowercase data

20. Making decisions can be made using:
  - single alternative
  - dual alternative
  - multiple alternative
  - all of the above


21. For each statement, enter a number from the column at the right that best matches the what the statement represents.

Number | Question | Answer
--|---|--
1. | A function available to determine how many items are in a sequence | len
2. | A part of a sequence |
3. | Used to repeat a set of instructions | loop
4. | A sequence of characters | string
5. | A sequence of strings or other data | tuple
6. | Used to place comments in your program | #
7. | A number without decimal places | integer
8. | Used to ask for user input | input
9. | Used to create a new line | \n
10. | Data type that can only contain True or False | boolean

  - ~integer~
  - ~string~
  - len
  - tuple
  - ~boolean~
  - ~input~
  - slice
  - ~#~
  - ~loop~
  - ~\n~


22. List four (4) attributes that every variable has:



23. List and give a simple example of three built-in functions used for converting data types and values:


24. When using strings, there are many methods provided by Python to alter the value of the string by creating a new string. List three (3) of these methods and describe what each does. (hint: consider the “case” of a string)


25. List and describe the two (2) keywords that we have used in class for creating loops. How are they similar and how are they different in structuring a loop?



26. Select two(2) terms from the following list and describe what they are.
true block	  concatenation	 tuple  	escape sequence


27. Describe what the following code does:

```python
{
sampleTuple=("ABC", "DEF", "HIJ", "KLM")
print (sampleTuple)
print (sampleTuple[1])
print (sampleTuple[2:])
print (sampleTuple[0:4])
for element in sampleTuple:
    print (element.lower())
for element in sampleTuple:
    print (element[0])
print (len(sampleTuple))
}
```

28. Describe what the following code does:


```python
{
firstName = input("enter your first name")
lastName = input("enter your last name")
if firstName == "":
    print ("you didn't enter a first name")
if lastName == "":
    print ("you didn't enter a last name")
fullName=firstName + lastName
nameLen=len(fullName)
print ("your name is " + str(nameLen) + " characters long")
for letter in fullName:
    print (letter)
}
```
