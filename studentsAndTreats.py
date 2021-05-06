"""
This function takes 3 parameters,
numberOfStudents, treats and startingChair. 
It returns the lastStudent chair number
"""

def getLastStudent(numberOfStudents, treats, startingChair):
    treats %= numberOfStudents
    lastStudent = (treats + startingChair - 1) % numberOfStudents 
    if lastStudent == 0:                          
        lastStudent = numberOfStudents
    return lastStudent