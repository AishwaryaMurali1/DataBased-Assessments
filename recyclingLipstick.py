"""
This function takes two parameters
numberofLipsticks - Gives the initial number of lipsticks
numberOfLeftoversNeeded - Gives the number of leftovers needed to make a new lipstick
Returns totalNumberOfLipsticks
"""

def getTotalNumOfLipsticks(numberOfLipsticks, numberOfLeftoversNeeded):
    totalNumberOfLipsticks = numberOfLipsticks
    while numberOfLipsticks>=numberOfLeftoversNeeded:
        totalNumberOfLipsticks+= numberOfLipsticks//numberOfLeftoversNeeded
        numberOfLipsticks = numberOfLipsticks//numberOfLeftoversNeeded + numberOfLipsticks%numberOfLeftoversNeeded
    return totalNumberOfLipsticks