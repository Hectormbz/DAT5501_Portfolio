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

