import streamlit as st
import pandas as pd
import plotly.express as px
from data_visualization import show_histogram, show_scatter_plot, show_pair_plot

histogram, scatter, pair = st.tabs(["Histogram", "Scatter Plot", "Pair Plot"])

with histogram:
    st.header("Histogram")
    if "df" in st.session_state and st.session_state.df is not None:
        show_histogram(st.session_state.df)
    else:
        st.warning("Please upload a CSV file in the main page first.")

with scatter:
    st.header("Scatter Plot")
    if "df" in st.session_state and st.session_state.df is not None:
        show_scatter_plot(st.session_state.df)
    else:
        st.warning("Please upload a CSV file in the main page first.")

with pair:
    st.header("Pair Plot")
    if "df" in st.session_state and st.session_state.df is not None:
        show_pair_plot(st.session_state.df)
    else:
        st.warning("Please upload a CSV file in the main page first.")
