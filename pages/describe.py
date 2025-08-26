import streamlit as st
import pandas as pd

csv_data = st.file_uploader("Upload your CSV file", type=["csv"])

if csv_data is not None:
    df = pd.read_csv(csv_data)
    described_data = df.describe().T.reset_index() # change to new function
    st.dataframe(described_data)