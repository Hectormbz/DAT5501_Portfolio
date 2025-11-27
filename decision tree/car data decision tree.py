from ucimlrepo import fetch_ucirepo
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report

# Load dataset
car_evaluation = fetch_ucirepo(id=19)
df = car_evaluation.data.features.copy()

#Encoding dictionaries
encodeBuying = {"low": 0, "med": 1, "high": 2, "vhigh": 3}
encodeMaint = {"low": 0, "med": 1, "high": 2, "vhigh": 3}
encodeDoors = {"2": 0, "3": 1, "4": 2, "5more": 3}
encodePersons = {"2": 0, "4": 1, "more": 2}
encodeLug = {"small": 0, "med": 1, "big": 2}

#Encoding
df["buying"] = df["buying"].map(encodeBuying)
df["maint"] = df["maint"].map(encodeMaint)
df["doors"] = df["doors"].map(encodeDoors)
df["persons"] = df["persons"].map(encodePersons)
df["lug_boot"] = df["lug_boot"].map(encodeLug)


#Set safety as the target
y = df["safety"]
X = df.drop(columns=["safety"])

#Train-test split
splitPoint = int(0.8*len(X))

Xtrain = X[:splitPoint]
yTrain = y[:splitPoint]

Xtest = X[splitPoint:]
yTest = y[splitPoint:]

#Train decision tree
model = DecisionTreeClassifier()
model.fit(Xtrain, yTrain)

#Evaluate to find precision, recall and F1
yPred = model.predict(Xtest)

print("Classification Report:")
print(classification_report(yTest, yPred))