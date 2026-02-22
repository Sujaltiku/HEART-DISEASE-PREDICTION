#  Heart Disease Prediction System

A Machine Learning web application that predicts the likelihood of heart disease using clinical patient data.
The model is trained using Logistic Regression and deployed with a Streamlit interface for real-time prediction.

---

##  Project Overview

This project demonstrates an end-to-end ML workflow:

* Data preprocessing and training done in **`model.ipynb`**
* Model saved as **`.joblib`**
* Interactive prediction interface built using **Streamlit**
* Binary classification output:

  *  No Defect Detected
  *  High Risk of Heart Disease

---

##  Features Used for Prediction

| Feature  | Description                       |
| -------- | --------------------------------- |
| age      | Age of the patient                |
| sex      | Gender (0 = Female, 1 = Male)     |
| cp       | Chest pain type                   |
| trestbps | Resting blood pressure            |
| chol     | Cholesterol level                 |
| fbs      | Fasting blood sugar > 120 mg/dl   |
| restecg  | Resting ECG results               |
| thalach  | Maximum heart rate achieved       |
| exang    | Exercise induced angina           |
| oldpeak  | ST depression                     |
| slope    | Slope of peak exercise ST segment |
| ca       | Number of major vessels           |
| thal     | Thalassemia                       |

---

##  Model Information

* Algorithm: **Logistic Regression**
* Type: Binary Classification
* Output: `0 = No Disease`, `1 = Disease`
* Model saved using: `joblib`

---

##  How to Run This Project Locally

### Step 1 — Clone the Repository

```bash
git clone https://github.com/your-username/heart-disease-prediction.git
cd heart-disease-prediction
```

---

### Step 2 — Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Step 3 — Run the Streamlit App

```bash
streamlit run app.py
```

App will open in your browser at:

```
http://localhost:8501
```

---

##  Training the Model

To retrain the model:

1. Open:

```
model.ipynb
```

2. Run all cells.
3. The trained model will be saved as:

```
model.joblib
```

---

##  Application Interface

The web interface allows users to:

* Enter patient clinical parameters
* Predict heart disease risk instantly
* View probability-based results
* Get a simple medical-style decision output

---

##  Project Structure

```
heart-disease-prediction/
│
├── model.ipynb   
├── model.joblib       
├── app.py             
├── requirements.txt  
├── README.md          
```

---

##  Purpose of This Project

This project is built for:

* Learning ML model deployment
* Demonstrating healthcare prediction systems
* Academic and portfolio showcase
* Understanding full ML lifecycle (Train → Save → Deploy)

---

##  Future Improvements

* Add Explainable AI (SHAP)
* Deploy on cloud (Streamlit Cloud / AWS)
* Add batch prediction via CSV upload
* Improve UI with medical visualization
* Add model comparison (SVM, Random Forest)

---

##  Author

**Your Name**

Machine Learning Enthusiast
Focused on building real-world AI solutions.

---

##  License

This project is open-source and free to use for educational purposes.
