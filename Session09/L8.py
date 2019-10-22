filStudents = open(file="Students.txt",mode="r")
lstStudents = filStudents.readlines()
filStudents.close()

print(lstStudents)

for student in lstStudents:
    print(student.title())
