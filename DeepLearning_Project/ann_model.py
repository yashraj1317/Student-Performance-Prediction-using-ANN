import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier

# Load dataset
df = pd.read_csv("dataset.csv")

# Clean data
df = df.dropna()
df['Result'] = df['Result'].map({'Fail': 0, 'Pass': 1})

# Features
X = df[['Study_Hours', 'Attendance', 'Previous_Marks', 'Assignment_Score']]
y = df['Result']

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Scale
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# ANN Model (MLP)
model = MLPClassifier(hidden_layer_sizes=(16, 8), max_iter=500)
model.fit(X_train, y_train)

# Accuracy
accuracy = model.score(X_test, y_test)
print("Accuracy:", accuracy)

# Prediction
sample = scaler.transform([[5, 80, 70, 75]])
prediction = model.predict(sample)

print("Prediction:", "Pass" if prediction[0] == 1 else "Fail")