import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Reading the dataset
data = pd.read_csv('bigml_59c28831336c6604c800002a.csv')
st.title('Customer churn in the Telecom Industry')
st.subheader('This model predicts how likely a customer is likely to churn in the telco industry')

# Displaying the pie chart
counts = data['churn'].value_counts()
plt.figure(figsize =(12,8))
plt.pie(counts, labels=['Not Churned', 'Churned'], autopct='%1.1f%%', startangle=90)
plt.axis('equal')
plt.title('Distribution of churn across the Dataset in %')
plt.savefig('piechart.png')
st.image('piechart.png')