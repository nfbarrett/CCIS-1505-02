lstStudents = []
strName = input("Enter student to add to class: ")
lstStudents.append(strName.lower() + "\n") #create a line in the list

filStudents = open(file="Students.txt",mode="a")  #open file for appending
filStudents.writelines(lstStudents)  #write lines to (LSV) file
filStudents.close() #close file
print (lstStudents)


filStudents = open(file="Students.txt",mode="r")  #open file for reading
lstStudents = filStudents.readlines() #read lines into list (LSV file)
filStudents.close() #close file

lstStudents.sort()

print (lstStudents)











