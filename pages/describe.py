import streamlit as st
import pandas as pd
from stats.table_stats import stats_table

csv_data = st.file_uploader("Upload your CSV file", type=["csv"])

if csv_data is not None:
    df = pd.read_csv(csv_data)
    described_data = stats_table(df)
    st.dataframe(described_data)