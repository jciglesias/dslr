import streamlit as st
import pandas as pd

csv_data = st.file_uploader("Upload your CSV file", type=["csv"])

if csv_data is not None:
    df = pd.read_csv(csv_data)
    described_data = df.describe().T.reset_index() # change to new function
else:
    described_data = {
        'statistics': ['count','mean', 'std', 'min','P25', 'P50', 'P75', 'max'],
        'Feature1': range(8),
        'Feature2': range(10,18),
        'Feature3': range(20,28),
        'Feature4': range(30,38),
}

st.dataframe(described_data)