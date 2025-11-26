import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Load CSV file
df = pd.read_csv(r'C:\Users\hbuzzacott001\OneDrive - PwC\Uni work\YR2\DAT5501_Portfolio\life expectancy project\life-expectancy.csv', sep=',')

#Convert 'Year' column to integer
df['Year'] = df['Year'].astype(int)

#Filter the DataFrame for entries after 1922
filteredDF = df[df['Year'] > 1923]

#split data into training data and data to use for comparison
subSampleDF = filteredDF[filteredDF['Year'] < 2014]
compareDF = filteredDF[filteredDF['Year'] > 2013]


yearsTrain = subSampleDF['Year'].values
lifeExpectancyTrain = subSampleDF['Period life expectancy at birth'].values

totalYears = filteredDF['Year'].values
totalLifeExpectancy = filteredDF['Period life expectancy at birth'].values

#Set up plot
plt.figure(figsize=(12, 8))
plt.plot(totalYears, totalLifeExpectancy, 'o', label='Observed data')

#fullYears = np.arange(1924, 2024)

chiSquaredPerDoF = []
BayesianIC = []

#Fit polynomials of order 1 to 9
for order in range(1, 10):
    coeffs = np.polyfit(yearsTrain, lifeExpectancyTrain, order)
    poly = np.poly1d(coeffs)
    forecast = poly(totalYears)
    lifeExpectancyModel = poly(yearsTrain)
    
    #Plot the polynomial forecast
    plt.plot(totalYears, forecast, label=f'Order {order} Forecast')

    #Calculate residuals
    residuals = lifeExpectancyTrain - lifeExpectancyModel
    
    #Calculate chi-squared with estimated uncertainty
    chiSquared = np.sum((residuals ** 2) / 0.5**2)
    
    #Calculate degrees of freedom
    dof = 90 - (order + 1)
    
    #Calculate chi-squared per degree of freedom
    chiSquaredPerDoF.append(chiSquared / dof)

    #Calculate Bayesian Information Criterion
    BayesianIC.append(chiSquared + (order + 1)*(np.log(90)))

#add vertical line to indicate start of prediction
plt.axvline(x=2014, color='red', linestyle='--', label='Start of Prediction')

#plot life expectancy predictions
plt.title('Life Expectancy Forecasts using Polynomials')
plt.xlabel('Year')
plt.ylabel('Life Expectancy')
plt.legend(loc='upper left')
plt.grid(True)
plt.show()

#Plot Chi-squared per degree of freedom
plt.figure(figsize=(10, 6))
plt.plot(range(1, 10), chiSquaredPerDoF, marker='o')
plt.title('Chi-Squared per Degree of Freedom for Polynomial Orders')
plt.xlabel('Polynomial Order')
plt.ylabel('Chi-Squared per Degree of Freedom')
plt.grid(True)
plt.show()

#Plot Bayesian Information Criterion
plt.figure(figsize=(10, 6))
plt.plot(range(1, 10), BayesianIC, marker='o')
plt.title('Bayesian Information Criterion for Polynomial Orders')
plt.xlabel('Polynomial Order')
plt.ylabel('Bayesian Information Criterion') 
plt.grid(True)
plt.show()
