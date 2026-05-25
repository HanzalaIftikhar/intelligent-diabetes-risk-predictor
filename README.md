# 🩺 Intelligent Diabetes Risk Predictor

An end-to-end Machine Learning web app that predicts whether a patient 
is at risk of diabetes using clinical health data.

> Final Year Project (FYP) — BS Computer Science  
> Virtual University, Lahore

---

## 🎯 Project Overview
This system takes patient health information such as Glucose level, 
Blood Pressure, BMI, Age, etc. and predicts:
- ✅ Non-Diabetic (Low Risk)
- 🟡 Possibly Diabetic (Medium Risk)  
- 🔴 Diabetic (High Risk)

Along with personalized health recommendations.

---

## 📊 Dataset
- **Source:** Kaggle — Pima Indians Diabetes Dataset
- **Rows:** 768 patients
- **Features:** Glucose, Blood Pressure, BMI, Age, Pregnancies, etc.
- **Target:** Diabetic (1) or Non-Diabetic (0)
- **Preprocessing:** Zero values fixed, SMOTE applied for class balancing

---

## 🤖 Models Trained & Compared
| Model | Accuracy | Precision | Recall | F1 Score |
|---|---|---|---|---|
| Logistic Regression | 70.1% | 55.9% | 65.0% | 60.1% |
| Decision Tree | 69.7% | 54.9% | 70.0% | 61.5% |
| **SVM ✅ Best** | **71.4%** | **56.5%** | **76.3%** | **64.9%** |

**Winner: SVM** — selected based on highest Recall and F1 Score.  
In medical diagnosis, Recall is most important — missing a diabetic 
patient is dangerous.

---

## 🖥️ App Features
- 🔍 Diabetes risk prediction (Low / Medium / High)
- 📋 Personalized health recommendations
- 📊 Dashboard — model performance comparison
- ℹ️ About page — project info

---

## ⚙️ Tech Stack
- **Language:** Python
- **ML:** Scikit-learn, imbalanced-learn (SMOTE)
- **App:** Streamlit
- **Data:** Pandas, NumPy
- **Visualization:** Matplotlib, Seaborn

---

## 🚀 How to Run
```bash
# Clone the repo
git clone https://github.com/HanzalaIftikhar/intelligent-diabetes-risk-predictor.git

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

---

## 👨‍💻 Developer
**Hanzala Iftikhar**  
BS Computer Science — Virtual University, Lahore  
📧 ranahanzala327@gmail.com  
🔗 [LinkedIn](https://linkedin.com/in/hanzala-iftikhar-783149213/)  
🐙 [GitHub](https://github.com/HanzalaIftikhar)

---

## ⚠️ Disclaimer
This system is for educational purposes only and does not replace 
professional medical advice. Always consult a qualified doctor.