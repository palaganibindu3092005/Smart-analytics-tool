import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.set_page_config(page_title="Smart Analytics Tool", layout="wide")
st.title("📊 Smart Analytics Tool - Week 2 Project 3")

# 1. CSV Upload Feature
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    # 2. Dataset Preview
    st.subheader("1️⃣ Dataset Preview")
    st.write(f"Shape: {df.shape[0]} rows, {df.shape[1]} columns")
    st.dataframe(df.head())
    
    # 3. Missing Value Analysis
    st.subheader("2️⃣ Missing Value Analysis")
    missing = df.isnull().sum()
    missing_df = pd.DataFrame({
        'Column': missing.index,
        'Missing Values': missing.values,
        'Percentage': (missing.values / len(df) * 100).round(2)
    })
    st.dataframe(missing_df[missing_df['Missing Values'] > 0])
    if missing.sum() == 0:
        st.success("No missing values found! ✅")
    
    # 4. Basic Statistical Summary
    st.subheader("3️⃣ Statistical Summary")
    st.dataframe(df.describe())
    
    # 5. 3 Dynamic Visualizations
    st.subheader("4️⃣ Dynamic Visualizations")
    
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    cat_cols = df.select_dtypes(include=['object']).columns.tolist()
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.write("**Bar Chart**")
        if cat_cols and numeric_cols:
            x_cat = st.selectbox("Category", cat_cols, key='bar_x')
            y_num = st.selectbox("Value", numeric_cols, key='bar_y')
            fig = px.bar(df, x=x_cat, y=y_num, title=f"{y_num} by {x_cat}")
            st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.write("**Pie Chart**")
        if cat_cols:
            pie_col = st.selectbox("Select Column", cat_cols, key='pie')
            fig = px.pie(df, names=pie_col, title=f"Distribution of {pie_col}")
            st.plotly_chart(fig, use_container_width=True)
    
    with col3:
        st.write("**Scatter Plot**")
        if len(numeric_cols) >= 2:
            x_scatter = st.selectbox("X-axis", numeric_cols, key='sc_x')
            y_scatter = st.selectbox("Y-axis", numeric_cols, index=1, key='sc_y')
            fig = px.scatter(df, x=x_scatter, y=y_scatter, title=f"{y_scatter} vs {x_scatter}")
            st.plotly_chart(fig, use_container_width=True)
            
else:
    st.info("👆 Please upload a CSV file to start analysis")
    st.write("**Test with:** Use your IPL.csv file")
