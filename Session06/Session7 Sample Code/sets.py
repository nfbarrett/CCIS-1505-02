lstClass1 = ["joe", "ann", "bob", "sue", "bill"]
lstClass2 = ["tim", "ann", "jim", "sue", "sam"]
setStudents1 = set(lstClass1)
setStudents2 = set(lstClass2)

setStudents3 = setStudents1.union(setStudents2) #union - joining sets (no duplicates)
print ( setStudents3 )


setStudents3.discard("bob")  #removes, with no keyError if not found
print ( setStudents3 )
print ( )

setStudents3.add("steve")
print ( setStudents3 )
print ( )

setStudents4 = setStudents1 | setStudents2  #union of two sets
print ( setStudents4 )
print ( )

setStudents5 = setStudents1.intersection(setStudents2) #intersection of sets 
print ( setStudents5 )
print ( )

setStudents6 = setStudents1.difference(setStudents2) #elements occuring in set1 but not set2
print ( setStudents6 )
print ( )

blnSubSet = setStudents1.issubset(setStudents2) #is set1 a subset of set2?
print ( blnSubSet )
print ( )

blnSubSet = setStudents1.issuperset(setStudents2) #is set1 a superset of set2?
print ( blnSubSet )
print ( )


