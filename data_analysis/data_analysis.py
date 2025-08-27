import streamlit as st
import pandas as pd
from .operations import operations

class DataAnalysis:
    def __init__(self):
        self.df = None
        self.csv_uploaded = False
        self.table_result = None

    def get_stats(self):
        """Return descriptive stats using stats_table if CSV exists"""
        if self.df is not None:
            whitelist = ["Arithmancy", "Astronomy", "Herbology", "Defense Against the Dark Arts", 
            "Divination", "Muggle Studies", "Ancient Runes", "History of Magic", "Transfiguration",
            "Potions", "Care of Magical Creatures", "Charms", "Flying"]
            self.table_result = self.stats_table(whitelist=whitelist)
            return self.table_result
        return None

    def stats_table(self, whitelist=None) -> pd.DataFrame:
        """
        self.df: pandas DataFrame to analyze
        whitelist: list of column names to include. If None, use all columns.
        """
        # Determine which columns to use
        if whitelist is None:
            columns_to_use = self.df.columns
        else:
            # Keep only columns that exist in df
            columns_to_use = [col for col in whitelist if col in self.df.columns]

        rows = []

        for col in columns_to_use:
            series = self.df[col]
            rows.append(operations(series))

        stats = pd.DataFrame(
            rows,
            index=columns_to_use,
            columns=['count','mean','std','min','P25','P50','P75','max']
        ).T

        return stats
