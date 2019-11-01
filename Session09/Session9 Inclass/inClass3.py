strName = input("Enter student to add to class: ")

filStudents = open(file="Students.txt",mode="a")  #open file for appending
filStudents.write(strName.lower() + "\n")  #write lines to (LSV) file
filStudents.close() #close file

filStudents = open(file="Students.txt",mode="r")  #open file for reading
lstStudents = filStudents.readlines() #read lines into list (LSV file)
filStudents.close() #close file
print (lstStudents)











