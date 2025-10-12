import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Calculating relative change from 1990-2024:


df = pd.read_csv("total-number-of-international-immigrants.csv")
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
plt.xticks(rotation=45, ha = "right")
plt.show()

#filtering for countries 