import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, mean_absolute_error
from sklearn.metrics import r2_score

#Load dataset
df = pd.read_csv(r"C:\Users\hbuzzacott001\OneDrive - PwC\Uni work\YR2\DAT5501_Portfolio\personal projects\pl-tables-1993-2024.csv")

#Sort by season
df = df.sort_values(["season_end_year", "team"])

#calculate performance trends
df["points_per_game"] = df["points"] / df["played"]
df["gd_per_game"] = df["gd"] / df["played"]
df["win_rate"] = df["won"] / df["played"]

#Create target labels
df["champion"] = (df["position"] == 1).astype(int)
df["top4"] = (df["position"] <= 4).astype(int)
df["relegated"] = (df["position"] >= 18).astype(int)

#Restrict to Chelsea
chelsea = df[df["team"] == "Chelsea"].sort_values("season_end_year")

#Predicting finishing position (Regression)

features = ["points_per_game", "gd_per_game", "win_rate", "gf", "ga", "points"]
X = chelsea[features]
yPosition = chelsea["position"]

#Train/test split
XTrain, XTest, yTrain, yTest = train_test_split(X, yPosition, test_size=0.25, random_state=20)

#Scale inputs
scaler = StandardScaler()
XTrainScaled = scaler.fit_transform(XTrain)
XTestScaled = scaler.transform(XTest)

reg = LinearRegression()
reg.fit(XTrainScaled, yTrain)

#Predict finishing positions based on performance metrics
posPred = reg.predict(XTestScaled)

print("\n Regression: Predicting Chelsea League Position")
#output the accuracy of the predictions
print("Mean absolute error:", mean_absolute_error(yTest, posPred))
r2 = r2_score(yTest, posPred)
print("R-squared:", r2)

#Predicting probabilities of champion, top 4 and relegated

#Use all-club data
XAll = df[features]
XAllScaled = scaler.fit_transform(XAll)

yChamp = df["champion"]
yTop4 = df["top4"]
yReleg = df["relegated"]

#Logistic regressions
champModel = LogisticRegression(max_iter=500)
top4Model = LogisticRegression(max_iter=500)
relegModel = LogisticRegression(max_iter=500)

champModel.fit(XAllScaled, yChamp)
top4Model.fit(XAllScaled, yTop4)
relegModel.fit(XAllScaled, yReleg)

#Train a more powerful non-linear model too
rf = RandomForestClassifier(n_estimators=300, random_state=42)
rf.fit(XAll, yTop4)

#Predict probabilities for the most recent Chelsea season
latest = chelsea.iloc[-1:][features]
latestScaled = scaler.transform(latest)

probWin = champModel.predict_proba(latestScaled)[0][1]
probTop4 = top4Model.predict_proba(latestScaled)[0][1]
probReleg = relegModel.predict_proba(latestScaled)[0][1]
probTop4rf = rf.predict_proba(latest)[0][1]

print("\nProbability Forecast For Chelsea Next Season")
print(f"Chance of WINNING the league:       {probWin:.2%}")
print(f"Chance of FINISHING TOP 4:          {probTop4:.2%}  (logistic)")
print(f"Chance of FINISHING TOP 4:          {probTop4rf:.2%}  (random forest)")
print(f"Chance of RELEGATION:               {probReleg:.2%}")

#Plot Chelsea finishing positions over time + predicted trend

plt.figure(figsize=(10,6))
plt.plot(chelsea["season_end_year"], chelsea["position"], marker="o", label="Actual Position")

# Predict trend line
XScaledAll = scaler.transform(X)
trend = reg.predict(XScaledAll)
plt.plot(chelsea["season_end_year"], trend, label="Predicted Trend", linestyle="--")

plt.gca().invert_yaxis()  # 1 = best
plt.title("Chelsea Finishing Position Over Time")
plt.xlabel("Season")
plt.ylabel("Position (1 = Champion)")
plt.grid(True)
plt.legend()
plt.show()


