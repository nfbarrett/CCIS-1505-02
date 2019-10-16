#Sample Program Using Functions


#Define functions
def DataEntry():
    """ This function asks the user for a list of the days of the week
    """
    weekdays = [ ]
    for lc in range(0,7):
        day=raw_input("Enter a day of the week: ")
        weekdays.append(day.title())
    return weekdays

def DataSort(listOfDays=[ ]):
    listOfDays.sort()
    return listOfDays

def DataPrint(listToPrint=[ ]):
    for day in listToPrint:
        print (day)

######Mainline Code
daysOfWeek=DataEntry()  #call function to get weekdays (input)
sortedDays=DataSort(listOfDays=daysOfWeek)  #call function to sort days (process)
DataPrint(listToPrint=sortedDays)  #call function to print sorted days (output)
