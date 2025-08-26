import streamlit as st
import pandas as pd
from stats.table_stats import stats_table

if "df" in st.session_state:
    df = st.session_state.df
    described_data = stats_table(df)
    st.dataframe(described_data)

else:
    st.write("Please upload a CSV file in the main app to see the data description.")