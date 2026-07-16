import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier

st.set_page_config(page_title="Student Performance Prediction", layout="centered")

st.title("Student Performance Prediction using ANN")
st.write("This mini project predicts whether a student will Pass or Fail.")

df = pd.read_csv("dataset.csv")

df["Result"] = df["Result"].map({"Fail": 0, "Pass": 1})

X = df[["Study_Hours", "Attendance", "Previous_Marks", "Assignment_Score"]]
y = df["Result"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = MLPClassifier(hidden_layer_sizes=(16, 8), max_iter=1000, random_state=42)
model.fit(X_train_scaled, y_train)

accuracy = model.score(X_test_scaled, y_test)

st.subheader("Model Accuracy")
st.success(f"{accuracy * 100:.2f}%")

st.subheader("Enter Student Details")

study_hours = st.number_input("Study Hours", min_value=1, max_value=10, value=5)
attendance = st.number_input("Attendance (%)", min_value=0, max_value=100, value=80)
previous_marks = st.number_input("Previous Marks", min_value=0, max_value=100, value=70)
assignment_score = st.number_input("Assignment Score", min_value=0, max_value=100, value=75)

if st.button("Predict Result"):
    sample = pd.DataFrame([{
        "Study_Hours": study_hours,
        "Attendance": attendance,
        "Previous_Marks": previous_marks,
        "Assignment_Score": assignment_score
    }])

    sample_scaled = scaler.transform(sample)
    prediction = model.predict(sample_scaled)

    if prediction[0] == 1:
        st.success("Predicted Result: Pass")
    else:
        st.error("Predicted Result: Fail")

st.subheader("Dataset Preview")
st.dataframe(df.head(20))