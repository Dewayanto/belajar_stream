import streamlit as st
import pandas as pd
import os
from data_processor import load_and_process_data
from fraud_detector import detect_fraud
from visualizer import plot_time_series, plot_amount_histogram, plot_description_bar

# Membuat folder data jika belum ada
if not os.path.exists("data"):
    os.makedirs("data")

st.title('Aplikasi Deteksi Kecurangan Keuangan')
st.write("Unggah file CSV Anda untuk mendeteksi transaksi yang berpotensi fraud.")

# File uploader
uploaded_file = st.file_uploader("Unggah file CSV Anda", type=["csv"])

if uploaded_file is not None:
    # Menyimpan file yang diunggah ke folder data
    file_path = os.path.join("data", uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    # Memuat dan memproses data
    df, X = load_and_process_data(file_path)
    
    # Memeriksa kolom yang diharapkan
    expected_columns = ['date', 'amount', 'description', 'account']
    if not all(col in df.columns for col in expected_columns):
        st.error("File yang diunggah harus memiliki kolom berikut: date, amount, description, account")
    else:
        # Mendeteksi kecurangan
        fraud_indices = detect_fraud(X)
        
        # Menampilkan transaksi yang terdeteksi sebagai kecurangan
        st.subheader("Transaksi yang Terdeteksi sebagai Kecurangan")
        fraud_df = df.iloc[fraud_indices]
        st.dataframe(fraud_df)
        
        # Visualisasi
        st.subheader("Visualisasi")
        fig_time = plot_time_series(df, fraud_indices)
        st.plotly_chart(fig_time)
        
        fig_hist = plot_amount_histogram(df, fraud_indices)
        st.plotly_chart(fig_hist)
        
        fig_bar = plot_description_bar(df, fraud_indices)
        st.plotly_chart(fig_bar)