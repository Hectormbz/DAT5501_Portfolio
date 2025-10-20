import numpy as np
def durationCalculator(userDate):

    ##get date from user as a string
    #userDate = input("Input date in the format YYYY-MM-DD: ")
    #convert to dateTime
    userDate = np.datetime64(userDate, 'D')
    #get today's date
    today = np.datetime64('today', 'D')
    #get difference
    difference = str(today - userDate)
    return difference




