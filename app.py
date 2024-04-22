import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

st.title('Customer Support Tickets Analysis')

# Upload and load the dataset
uploaded_file = st.file_uploader("Choose a CSV file for analysis", type="csv")
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write("Data Loaded Successfully!")

    # Replace inf values with NaN
    data.replace([np.inf, -np.inf], np.nan, inplace=True)

    # Option to display raw data
    if st.checkbox('Show raw data'):
        st.subheader("Raw Data")
        st.write(data)
        st.write("Column names in the dataset:", data.columns.tolist())  # Display column names

    # Distribution of Ticket Types by Age
    if st.checkbox('Show Distribution of Ticket Types by Age'):
        st.subheader('Distribution of Ticket Types by Age')
        # Create a facet grid for each ticket type
        g = sns.FacetGrid(data, col='Ticket Type', col_wrap=3, height=5, aspect=1.5)
        g.map(sns.histplot, 'Customer Age', bins=20, kde=True)
        g.set_titles('{col_name}')
        g.set_axis_labels('Age', 'Number of Tickets')
        st.pyplot(g)

    # Customer Satisfaction Distribution
    if st.checkbox('Show Customer Satisfaction Analysis'):
        st.subheader('Customer Satisfaction Distribution')
        fig, ax = plt.subplots()
        sns.histplot(data['Customer Satisfaction Rating'], bins=5, kde=True, color='skyblue')
        plt.title('Customer Satisfaction Distribution')
        st.pyplot(fig)

    # Tickets by Age Group
    if st.checkbox('Show Tickets by Age Group Analysis'):
        st.subheader('Tickets by Age Group')
        bins = [0, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        labels = ['0-20', '21-30', '31-40', '41-50', '51-60', '61-70', '71-80', '81-90', '91-100']
        data['Age Group'] = pd.cut(data['Customer Age'], bins=bins, labels=labels, right=False)
        age_group_counts = data['Age Group'].value_counts()
        fig, ax = plt.subplots()
        age_group_counts.plot(kind='bar', color='skyblue')
        plt.title('Tickets Raised by Age Group')
        st.pyplot(fig)

    # Ticket Status Distribution
    if st.checkbox('Show Ticket Status Distribution'):
        st.subheader('Ticket Status Distribution')
        ticket_status_counts = data['Ticket Status'].value_counts()
        fig, ax = plt.subplots()
        ticket_status_counts.plot(kind='bar', color='skyblue')
        plt.title('Ticket Status Distribution')
        st.pyplot(fig)
        
