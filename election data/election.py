import pandas as pd
import matplotlib.pyplot as plt

#load csv file
df = pd.read_csv(r"C:\Users\hbuzzacott001\OneDrive - PwC\Uni work\YR2\DAT5501_Portfolio\election data\US-2016-primary.csv", sep = ';')

#select candidate
candidateName = 'Bernie Sanders'
candidateDF = df[df['candidate'].str.contains(candidateName, na = False)]

# Group by state and candidate, sum votes
state_totals = df.groupby("state")["votes"].sum()
candidate_votes = candidateDF.groupby("state")["votes"].sum()

# Compute fraction of votes for the candidate per state
vote_fraction = (candidate_votes / state_totals).dropna()

# Plot histogram
plt.figure(figsize=(10, 6))
plt.hist(vote_fraction, bins=15, edgecolor='black')
plt.title(f"Histogram of Fraction of Votes for {candidateName} by State")
plt.xlabel("Fraction of Votes")
plt.ylabel("Number of States")
plt.grid(True, alpha=0.3)
plt.show()

