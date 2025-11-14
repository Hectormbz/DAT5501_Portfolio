import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load CSV file
df = pd.read_csv(r'C:\Users\hbuzzacott001\OneDrive - PwC\Uni work\YR2\DAT5501_Portfolio\life expectancy project\life-expectancy.csv', sep=',')

# Convert 'Year' column to integer
df['Year'] = df['Year'].astype(int)

# Filter the DataFrame for entries after 1922
filteredDF = df[df['Year'] > 1923]

# split data into training data and data to use for comparison
subSampleDF = filteredDF[filteredDF['Year'] < 2014]
compareDF = filteredDF[filteredDF['Year'] > 2013]


yearsTrain = subSampleDF['Year'].values
lifeExpectancyTrain = subSampleDF['Period life expectancy at birth'].values

compareYears = compareDF['Year'].values
compareLifeExpectancy = compareDF['Period life expectancy at birth'].values

# Set up plot
plt.figure(figsize=(12, 8))
plt.plot(compareYears, compareLifeExpectancy, 'o', label='Observed data')

future_years = np.arange(2014, 2024)
# Fit polynomials of order 1 to 9
for order in range(1, 10):
    coeffs = np.polyfit(yearsTrain, lifeExpectancyTrain, order)
    poly = np.poly1d(coeffs)
    forecast = poly(future_years)
    
    # Plot the polynomial forecast
    plt.plot(future_years, forecast, label=f'Order {order} Forecast')

# Finalize plot
plt.title('Life Expectancy Forecasts using Polynomials')
plt.xlabel('Year')
plt.ylabel('Life Expectancy')
plt.legend(loc='upper left')
plt.grid(True)
plt.show()


