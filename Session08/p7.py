# Programer: Nick Barrett
# Date Written: Oct 15, 2019
# Program Name: P7.py
# Company Name: HTC-CCIS1505


#### names
def Input():
    """This function get users's fn and ln and returns a string"""
    strFN = input("Enter your first name: ")
    strMN = input("Enter your middle name: ")
    strLN = input("Enter your last name: ")
    strFullName = strFN + " " + strMN + " " + strLN
    return strFullName


def Process(name):
    """This function received a name and returns it in title format"""
    strFullNameT = name.title()
    return strFullNameT

def Output(name):
    """This function recives a name and prints a greating message"""
    print("Hello,", name, "have a nice day!")


### calc for dimmensions

def BV(l=1,w=1,h=1,q=1):
    """This functions receives 0,1,2 or 3 parameters and returns box volume"""
    try:
        intVol = int(l) * int(w) * int(h) * int(q)
        return intVol
    except:
        return 0

##### scores

def GetScores():
    """This function collects scores from keyboard and returns a list of names"""
    lstScores = []
    blnDone = False
    while blnDone == False:
        strScore = input("Enter a score or press ENTER when done: ")
        if len(strScore) > 0:  #Did user enter a name
            lstScores.append(int(strScore))
        else:  #user pressed ENTER
            blnDone=True
    return lstScores

def AverageScore(lstScores):
##    results = list(map(int, lstScores))
    intAvScore = sum(lstScores) / len(lstScores)
    return intAvScore

def HighScore(lstScores):
##    results = list(map(int, lstScores))
    intHiScore = max(lstScores)
    return intHiScore

def LowScore(lstScores):
##    results = list(map(int, lstScores))
    intLoScore = min(lstScores)
    return intLoScore


######### end of functions #######


#step 1
print("Step 1")
strName= Input() #calls function and stores returned name in strName
print(strName)

strNameT = Process(strName)
print(strNameT)

Output(strNameT)
print()
print()


#step 2
print("Step 2")

lstData = GetScores()
lstData.sort()
print (lstData)

intAve = AverageScore(lstData)
intHigh = HighScore(lstData)
intLow = LowScore(lstData)
print("Average score is",intAve)
print("Hign score is",intHigh)
print("Low score is",intLow)

print()
print()

#step 3
print("Step 3")

strH = input("Enter box height: ")
strW = input("Enter box width: ")
strL = input("Enter box depth: ")
strQ = input("Enter how many boxes: ")


intBV = BV(l=strL, w=strW, h=strH, q=strQ)  #thre parameters passed in (length & width & height & quanity)
print ("Total Box volume(s) are: ", intBV)

print()
print()

