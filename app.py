import streamlit as st
import pandas as pd

st.set_page_config(page_title="DSLR App", page_icon=":bar_chart:", layout="wide")
st.title("DSLR App")

if "df" not in st.session_state:
    csv_data = st.file_uploader("Upload your CSV file", type=["csv"])
    if csv_data is not None:
        st.session_state.df = pd.read_csv(csv_data)

if 'df' in st.session_state and st.session_state.df is not None:
    st.dataframe(st.session_state.df)