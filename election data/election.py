import pandas as pd
import matplotlib.pyplot as plt

#load csv file
df = pd.read_csv("US-2016-primary.csv", sep = ';')

#select candidate
candidateName = 'Bernie Sanders'
candidateDF = df[df['candidate'].str.contains(candidateName, na = False)]

