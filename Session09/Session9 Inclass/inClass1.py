def ReadStudents(filename=""):
    try:
        filStudents = open(file=filename,mode="r")  #open file for reading
        lstStudents = filStudents.readlines() #read lines into list (LSV file)
        filStudents.close() #close file
        return lstStudents
    except(IOError):
        print ("Error opening/reading", filename)
        return None
######Mainline######
lstStudents = ReadStudents(filename="Students.txt")
if lstStudents != None:
    filStudents = open(file="Students.txt",mode="w")  #open file for writing
    filStudents.writelines(lstStudents)  #write lines to (LSV) file
    filStudents.close() #close file

    lstStudents = ReadStudents(filename="Students.txt")
    lstStudents.sort()
    print (lstStudents)











