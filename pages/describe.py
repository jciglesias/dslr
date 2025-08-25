import streamlit as st

tmp = {
    'statistics': ['count','mean', 'std', 'min','P25', 'P50', 'P75', 'max'],
    'Feature1': range(8),
    'Feature2': range(10,18),
    'Feature3': range(20,28),
    'Feature4': range(30,38),
}

st.dataframe(tmp)