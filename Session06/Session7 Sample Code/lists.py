weekdays=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
print ( "Entire list:" )
print ( weekdays )
print ( )
print ( "weekdays [4], which is acutally the 5th day")
print ( weekdays[4] )
print ( )
print ( "weekdays [1:4], which is acutally the 2nd, 3rd  and 4th days")
print ( weekdays[1:4])
print ()
print ( "weekdays [1:4], which is acutally the 2nd, 3rd  and 4th days")
print ( weekdays[1:4] )
print ()
print ( "change Firday to Freeday:")
weekdays[5]="Freeday" #change Friday to Freeday
print ( weekdays[5])
print ()
print ( "delete Freeday:")
del weekdays[5] #delete Freeday
print ( weekdays) #Show that Freeday is gone
print ()
print ( "weekdays with Friday appended:")
weekdays.append("Friday") #add Friday to the end of the list
print ( weekdays ) #Show the new list
print ()
print ( "weekdays sorted:" )
weekdays.sort()   #sort weekdays list
print ( weekdays)   #print ( sorted weekdays
print ( )
print ( "weekdays reversed:" )
weekdays.reverse()   #reverse weekdays list
print ( weekdays)   #print reversed weekdays
print ()
print ( "number of Tuesdays in weekday list:")
print ( weekdays.count("Tuesday"))#Tuesday in weekdays list
print ( )
print ( "insert Steveday after 2nd day -- before 3rd day")
weekdays.insert(2, "Steveday")   #insert Steveday weekdays list
print ( weekdays )  #print ( weekdays
print ( )
print ( "pop Steveday" )
print ( weekdays.pop(2) )  #pop Steveday from weekdays list
print ( weekdays) #print ( weekdays
print ()
print ( "remove Thursday")
weekdays.remove("Thursday")   #remove Thursday
print ( weekdays)   #print ( weekdays
print ()
