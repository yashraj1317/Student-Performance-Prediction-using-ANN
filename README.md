# 🎓 Student Performance Prediction using ANN

A Machine Learning web application that predicts whether a student is likely to **Pass** or **Fail** using an **Artificial Neural Network (ANN)**. The application is built with **Python**, **Scikit-learn**, and **Streamlit**, providing an interactive interface for entering student details and viewing predictions instantly.

---

## 📌 Features

- Predicts student performance (Pass/Fail)
- Interactive Streamlit web interface
- Artificial Neural Network (MLPClassifier)
- Displays model accuracy
- Dataset preview within the application
- Simple and user-friendly interface

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- Scikit-learn
- StandardScaler
- Artificial Neural Network (MLPClassifier)

---

## 📂 Project Structure

```
DeepLearning_Project/
│── app.py              # Streamlit application
│── ann_model.py        # ANN model training
│── dataset.csv         # Student dataset
│── README.md
```

---

## 📊 Dataset

The model is trained using the following student attributes:

- Study Hours
- Attendance
- Previous Marks
- Assignment Score

Target Variable:

- Result (Pass / Fail)

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/DeepLearning_Project.git
```

### 2. Navigate to the project folder

```bash
cd DeepLearning_Project
```

### 3. Install dependencies

```bash
pip install streamlit pandas scikit-learn
```

### 4. Run the application

```bash
-m streamlit run app.py
```

---

## 📷 Application Preview

Student Performance Prediction using ANN.png
Student Performance Prediction using ANN 2.png


## 📈 Model

The project uses an **Artificial Neural Network (ANN)** implemented with Scikit-learn's **MLPClassifier**.

### Model Configuration

- Hidden Layers: (16, 8)
- Activation Function: ReLU
- Optimizer: Adam
- Feature Scaling: StandardScaler

---

## 🎯 Prediction Process

1. Enter Study Hours
2. Enter Attendance Percentage
3. Enter Previous Marks
4. Enter Assignment Score
5. Click **Predict Result**
6. The model predicts whether the student will **Pass** or **Fail**

---

## 💡 Future Improvements

- Larger real-world dataset
- Deep Learning using TensorFlow/Keras
- Performance visualization charts
- Model comparison with other algorithms
- Deployment on Streamlit Cloud

---

## 👨‍💻 Author

**Yashraj Shedage**

M.Sc. Data Science Student

---

## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub.
