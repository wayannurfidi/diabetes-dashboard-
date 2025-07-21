import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Judul
st.title("Dashboard Diabetes Interaktif")

# Load data
df = pd.read_csv("cleaned_diabetes.csv")

# Sidebar - Filter
st.sidebar.header("Filter Data")
max_age = st.sidebar.slider("Usia Maksimal", 20, 80, 50)
min_bmi = st.sidebar.slider("BMI Minimum", 10.0, 60.0, 18.0)
max_glucose = st.sidebar.slider("Glucose Maksimum", 50, 200, 150)
min_bp = st.sidebar.slider("Blood Pressure Minimum", 20, 122, 60)

# Filter data
filtered_df = df[
    (df["Age"] <= max_age) &
    (df["BMI"] >= min_bmi) &
    (df["Glucose"] <= max_glucose) &
    (df["BloodPressure"] >= min_bp)
]

# Pilihan visualisasi
st.sidebar.header("Visualisasi")
viz_option = st.sidebar.selectbox("Pilih Visualisasi", ["Heatmap Korelasi", "Histogram Fitur"])

# Ringkasan Data
st.write("### Data Terfilter")
st.dataframe(filtered_df.head())

# Statistik Deskriptif
st.write("### Statistik Deskriptif")
st.write(filtered_df.describe())

# Visualisasi
if viz_option == "Heatmap Korelasi":
    st.write("### Heatmap Korelasi")
    fig1, ax1 = plt.subplots()
    sns.heatmap(filtered_df.corr(), annot=True, cmap="coolwarm", ax=ax1)
    st.pyplot(fig1)

elif viz_option == "Histogram Fitur":
    feature = st.selectbox("Pilih Fitur untuk Histogram", df.columns[:-1])
    st.write(f"### Histogram {feature}")
    fig2, ax2 = plt.subplots()
    sns.histplot(filtered_df[feature], kde=True, bins=30, ax=ax2)
    st.pyplot(fig2)

# Distribusi Outcome
st.write("### Distribusi Diabetes (0 = Negatif, 1 = Positif)")
st.bar_chart(filtered_df["Outcome"].value_counts())
