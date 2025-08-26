import streamlit as st
import pandas as pd
from data_analysis.data_analysis import DataAnalysis

def main():
    st.set_page_config(page_title="DSLR App", page_icon=":bar_chart:", layout="wide")
    st.title("DSLR App")

    # Initialize DataAnalysis instance in session_state
    if "data_analysis" not in st.session_state:
        st.session_state.data_analysis = DataAnalysis()

    data_analysis = st.session_state.data_analysis

    if "df" not in st.session_state:
        csv_data = st.file_uploader("Upload your CSV file", type=["csv"])
        if csv_data is not None:
            data_analysis.upload_csv(csv_data)

    if 'df' in st.session_state and st.session_state.df is not None:
        st.dataframe(st.session_state.df)

if __name__ == "__main__":
    main()