import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# page cinfiguration
st.set_page_config(page_title="Dashboard", page_icon="📊", layout="wide")

# title
st.title("Model Performance Dashboard")

# model comparison
models = ['Logistic Regression', 'Decision Tree', 'SVM']
accuracy = [0.7013, 0.6970, 0.7143]
precision = [0.5591, 0.5490, 0.5648]
recall = [0.6500, 0.7000, 0.7625]
f1 = [0.6012, 0.6154, 0.6489]

# Metrics Table
st.subheader("📋 Model Comparison Table")
df = pd.DataFrame({
    'Model': models,
    'Accuracy': accuracy,
    'Precision': precision,
    'Recall': recall,
    'F1 Score': f1
})

st.dataframe(df, use_container_width=True)

# Bar Chart
st.subheader("📈 Model Performance Chart")
fig, ax = plt.subplots(figsize=(10, 5))
x = np.arange(len(models))
width = 0.2

ax.bar(x - 0.3, accuracy, width, label='Accuracy')
ax.bar(x - 0.1, precision, width, label='Precision')
ax.bar(x + 0.1, recall, width, label='Recall')
ax.bar(x + 0.3, f1, width, label='F1 Score')

ax.set_xticks(x)
ax.set_xticklabels(models)
ax.set_ylim(0, 1)
ax.legend()
ax.set_title('Model Comparison')
st.pyplot(fig)

# Best Model
st.subheader("🏆 Best Model")
st.success("SVM - Selected as best model based on highest Recall (76.25%) and F1 Score (64.89%)")
st.info("In medical diagnosis, Recall is most important - missing a diabetic patient is dangerous.")