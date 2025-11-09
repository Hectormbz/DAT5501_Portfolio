import numpy as np
import pandas as pd
import os
import csv
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

#function for dates from random file

def durationCalculatorfromFile(fileDate):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(fileDate, header=None)
    today = np.datetime64('today', 'D')
    for i in range(20):
        # Access the date
        specificDate = df.iloc[i, 0]
        # Convert the date from DD/MM/YYYY to a pandas datetime object
        convertedDate = pd.to_datetime(specificDate, format='%d/%m/%Y')
        print("Date ", i + 1, " is ", today-convertedDate, " in the past")

     
durationCalculatorfromFile(r"C:\Users\hbuzzacott001\OneDrive - PwC\Uni work\YR2\DAT5501_Portfolio\duration calculator\random_dates.csv")       
    


