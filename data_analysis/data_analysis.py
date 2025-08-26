import streamlit as st
import pandas as pd
from .table_stats import stats_table

class DataAnalysis:
    def __init__(self):
        self.df = None
        self.csv_uploaded = False

    def upload_csv(self, csv_file):
        """Load CSV file into DataFrame and set uploaded flag"""
        if csv_file is not None:
            csv_file.seek(0) # Restart pointer
            self.df = pd.read_csv(csv_file)
            st.session_state.df = self.df
            self.csv_uploaded = True

    def get_stats(self):
        """Return descriptive stats using stats_table if CSV exists"""
        if self.csv_uploaded and self.df is not None:
            return stats_table(self.df)
        return None
