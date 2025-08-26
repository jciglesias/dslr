import streamlit as st
import pandas as pd
from .stats_table import stats_table

class DataAnalysis:
    def __init__(self):
        self.df = None
        self.csv_uploaded = False
        self.table_result = None

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
            whitelist = ["Arithmancy", "Astronomy", "Herbology", "Defense Against the Dark Arts", 
            "Divination", "Muggle Studies", "Ancient Runes", "History of Magic", "Transfiguration",
            "Potions", "Care of Magical Creatures", "Charms", "Flying"]
            self.table_result = stats_table(self.df, whitelist=whitelist)
            return self.table_result
        return None
