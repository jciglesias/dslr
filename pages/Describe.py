import streamlit as st
from data_analysis.data_analysis import DataAnalysis

def show_describe():
    """Display descriptive statistics from the uploaded CSV."""
    if "data_analysis" in st.session_state:
        data_analysis = st.session_state.data_analysis

        if data_analysis.csv_uploaded:
            described_data = data_analysis.get_stats()
            st.dataframe(described_data)
        else:
            st.write("Please upload a CSV file in the main app to see the data description.")
    else:
        st.write("Please upload a CSV file in the main app to see the data description.")

# Describe function
show_describe()
