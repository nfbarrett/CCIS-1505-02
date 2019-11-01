import pickle #imports code tor read/write binary (complex) files

lstNums = [77.25, 12.6, 85.32, 21.89]

filNums = open(file="Numbers.dat", mode="wb")
pickle.dump(lstNums, filNums)
filNums.close()

filNums = open(file="Numbers.dat", mode="rb")
lstNums = pickle.load(filNums)
filNums.close()
lstNums.sort()
print (lstNums)
