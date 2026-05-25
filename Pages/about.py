import streamlit as st

# page configuration
st.set_page_config(page_title="About", page_icon="ℹ️", layout="centered")

# title
st.title("ℹ️ About This Project")

# project description
st.markdown("""
## Intelligent Diabetes Risk Predictor

This system uses Machine Learning to predict whether a patient 
is at risk of diabetes based on their health information.

---

## 🎯 Project Goal
Early detection of diabetes to help patients and healthcare 
providers take timely action.

---

## 📊 Dataset
- **Source:** Kaggle — Pima Indians Diabetes Dataset
- **Rows:** 768 patients
- **Features:** Glucose, Blood Pressure, BMI, Age, etc.
- **Target:** Diabetic (1) or Non-Diabetic (0)

---

## 🤖 Models Used
| Model | Accuracy | Recall |
|---|---|---|
| Logistic Regression | 70.1% | 65.0% |
| Decision Tree | 69.7% | 70.0% |
| SVM ✅ | 71.4% | 76.3% |

**Best Model: SVM** — selected based on highest Recall

---

## ⚙️ Tech Stack
- Python
- Scikit-learn
- Streamlit
- Pandas, NumPy
- Matplotlib, Seaborn

---

## 👨‍💻 Developer
**Hanzala Iftikhar**  
BS Computer Science — Virtual University, Lahore  
📧 ranahanzala327@gmail.com  
🔗 [LinkedIn](https://linkedin.com/in/hanzala-iftikhar-783149213/)      
🔗 [GitHub](https://github.com/HanzalaIftikhar)

---

## ⚠️ Disclaimer
This system is for educational purposes only and does not 
replace professional medical advice.
""")