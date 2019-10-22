##### scores

def GetScores():
    """This function collects scores from keyboard and returns a list of names"""
    lstScores = []
    blnDone = False
    while blnDone == False:
        intScore = input("Enter a score or press ENTER when done: ")
        if len(intScore) > 0:  #Did user enter a name
            lstScores.append(intScore)
        else:  #user pressed ENTER
            blnDone=True
    return lstScores

def AverageScore(lstScores):
    results = list(map(int, lstScores))
    intAvScore = sum(results) / len(results)
    return intAvScore

def HighScore(lstScores):
    results = list(map(int, lstScores))
    intHiScore = max(results)
    return intHiScore

def LowScore(lstScores):
    results = list(map(int, lstScores))
    intLoScore = min(results)
    return intLoScore


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
