import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Calculating relative change from 1990-2024:


df = pd.read_csv(r"C:\Users\hbuzzacott001\OneDrive - PwC\Uni work\YR2\DAT5501_Portfolio\immigration project\total-number-of-international-immigrants.csv")
numImmigrants = "Total number of international immigrants"

#get values for each year:

df1990 = df[df["Year"] == 1990][["Entity", numImmigrants]].rename(columns = {numImmigrants: "num1990"})
df2024 = df[df["Year"] == 2024][["Entity", numImmigrants]].rename(columns = {numImmigrants: "num2024"})

#create data set with just those years:

newData = pd.merge(df1990, df2024, on="Entity")

#Calculate relative increase

newData["RelativeChange(%)"] = ((newData["num2024"] - newData["num1990"]) / newData["num1990"]) * 100

#Draw graph for every country

colours = ["blue" if c != "United Kingdom" else "red" for c in newData["Entity"]]

plt.bar(newData["Entity"], newData["RelativeChange(%)"], color = colours)
plt.xlabel("Country")
plt.ylabel("Relative change 1990 - 2024 (%)")
plt.title("Relative change in immigrants living in each country")
plt.show()

#filtering for countries 

Countries = ["Chile", "Turkey", "Hungary", "United Kingdom", "Poland", "France", "South Korea", "Germany", "India", "Canada", "Australia", "United States", "Netherlands", "Belgium", "Spain", "Sweden", "Italy", "South Africa", "Singapore", "Japan", "Malaysia", "Colombia", "Peru", "Brazil", "Thailand", "Indonesia"]
filtered = newData[newData["Entity"].isin(Countries)]

#sort by relative change

filtered = filtered.sort_values("RelativeChange(%)", ascending = True)

#Plot filtered chart

concernedCountries = ["Chile", "Turkey", "Hungary"]
filteredColours = []
for c in filtered["Entity"]:
    if c == "United Kingdom":
        filteredColours.append("red")
    elif c in concernedCountries:
        filteredColours.append("orange")
    else:
        filteredColours.append("Blue")
        
plt.bar(filtered["Entity"], filtered["RelativeChange(%)"], color = filteredColours)
plt.xlabel("Country")
plt.ylabel("Relative change 1990 - 2024 (%)")
plt.title("Relative change in immigrants living in each country")
plt.xticks(rotation = 40, ha = "right")
