import pickle
try:
    filStudents = open(file="Students.txt",mode="r")  #open file for reading
    lstStudents = filStudents.readlines() #read lines into list (LSV file)
    filStudents.close() #close file
except(IOError):
    print ("Error opening/reading Students.txt file!")
    quit()

print (lstStudents)

try:
    filStudents = open(file="Y:\Students.dat",mode="wb")  #open file for binary writing
    pickle.dump(lstStudents, filStudents)  #write (dump) binary to file
    filStudents.close() #close file
except(IOError):
    print ("Error opening/dumping Students.dat file!")
    quit()












