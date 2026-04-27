# 🏦 Bank Loan Prediction System

##  Project Description

The **Bank Loan Prediction System** is a Machine Learning project that predicts whether a loan will be **Approved** or **Rejected** based on customer details like income, credit history, loan amount, etc.

This project includes:

* Data Preprocessing
* Exploratory Data Analysis (EDA)
* Machine Learning Model (Random Forest)
* Flask API
* Streamlit App
* Web Frontend (HTML, CSS, JavaScript)

---

##  Features

* 🔍 Customer Data Input
* 🤖 Loan Approval Prediction
* 📊 Probability Score
* 🌐 REST API using Flask
* 🎨 Interactive UI (Streamlit + Web)
* 📈 Data Visualization (EDA)

---

## 🧠 Machine Learning Model

* Algorithm: **Random Forest Classifier**
* Data Split: 80% Training / 20% Testing
* Model Saved using **Pickle**
* Evaluation Metric: Accuracy Score

---

## 📂 Project Structure

```
Loan-Prediction-System/
│
├── data/
│   ├── loan_data.csv
│   └── cleaned_loans_data.csv
│
├── models/
│   └── loan_model.pkl
│
├── backend/
│   └── app.py
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── streamlit_app.py
├── preprocessing.py
├── model_training.py
├── eda.py
│
└── README.md
```

---



### 1. Install Dependencies

```bash
pip install flask streamlit pandas numpy scikit-learn matplotlib seaborn
```

---

## How to Run

### Run Flask API

```bash
python app.py
```

API will run on:

```
http://127.0.0.1:5000/
```

---

### Run Streamlit App

```bash
streamlit run streamlit_app.py
```

---

### Run Frontend

Open:

```
index.html
```

---

## API Endpoint

### POST `/predict`

### Request Example:

```json
{
  "gender": 1,
  "married": 1,
  "dependents": 0,
  "education": 0,
  "self_employed": 0,
  "income": 5000,
  "co_income": 0,
  "loan_amount": 200,
  "loan_term": 360,
  "credit": 1,
  "area": 2
}
```

### Response Example:

```json
{
  "prediction": 1,
  "probability": 0.85
}
```

---

## Exploratory Data Analysis (EDA)

* Missing Values Heatmap
* Loan Approval Count Plot
* Income Distribution
* Correlation Matrix

---

## Data Preprocessing

* Removed unnecessary columns (Loan_ID)
* Handled missing values (mean/mode)
* Converted categorical data using Label Encoding
* Saved cleaned dataset

---

## Model Training

* Train/Test Split
* Random Forest Model Training
* Accuracy Evaluation
* Model saved as `.pkl`

---

## Frontend

* HTML for structure
* CSS for styling
* JavaScript for API integration
* Real-time prediction results

---

## Example Output

* Loan Approved (85%)
* Loan Rejected (40%)

---

## Future Improvements

* User Authentication System
* Cloud Deployment (AWS / Render)
* Advanced UI (React / Tailwind)
* Multiple ML Models
* Database Integration

---


