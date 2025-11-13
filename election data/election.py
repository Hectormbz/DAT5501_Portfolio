import pandas as pd
import matplotlib.pyplot as plt

#load csv file
df = pd.read_csv(r"C:\Users\hbuzzacott001\OneDrive - PwC\Uni work\YR2\DAT5501_Portfolio\election data\US-2016-primary.csv", sep = ';')

#select candidate
candidateName = 'Bernie Sanders'
#select candidate to compare
compareCandidateName = 'Hillary Clinton'

candidateDF = df[df['candidate'].str.contains(candidateName, na = False)]
compareCandidateDF = df[df['candidate'].str.contains(compareCandidateName, na = False)]

# Group by state and candidate, sum votes
stateTotals = df.groupby("state")["votes"].sum()
candidateVotes = candidateDF.groupby("state")["votes"].sum()
compareCandidateVotes = compareCandidateDF.groupby("state")["votes"].sum()

# Compute fraction of votes for the candidate per state
voteFraction = (candidateVotes / stateTotals).dropna()
compareVoteFraction = (compareCandidateVotes / stateTotals).dropna()

# Plot histogram
plt.figure(figsize=(10, 6))
plt.hist(voteFraction, bins=15, edgecolor='black', alpha=0.7, label=candidateName, color='skyblue')
plt.hist(compareVoteFraction, bins=15, edgecolor='black', alpha=0.7, label=compareCandidateName, color='lightcoral')
plt.title(f"Histogram of Fraction of Votes for by State")
plt.xlabel("Fraction of Votes")
plt.ylabel("Number of States")
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()

#not sure what the histogram shows so here is a bar chart that shows each state

# Plot bar chart
plt.figure(figsize=(12, 6))
voteFraction.plot(kind='bar', color='skyblue', edgecolor='black', alpha = 0.7, label=candidateName)
compareVoteFraction.plot(kind='bar', color='lightcoral', edgecolor='black', alpha = 0.7, label=compareCandidateName)

# Format the plot
plt.title(f"Fraction of Votes by State")
plt.xlabel("State")
plt.ylabel("Fraction of Votes")
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.4)
plt.legend()

# Show the plot
plt.tight_layout()
plt.show()
