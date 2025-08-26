# stats_functions.py

import pandas as pd
from typing import List

def ft_count(series: pd.Series) -> int:
    """
    Count non-missing values in a pandas Series.
    Equivalent to pandas' series.count()
    """
    count = 0
    for val in series:
        if pd.notna(val):  # ignore NaN / None
            count += 1
    return count

def ft_mean(series: pd.Series) -> float:
    """Calculate the mean of the series"""
    pass  # TODO: implement

def ft_std(series: pd.Series) -> float:
    """Calculate the standard deviation of the series"""
    pass  # TODO: implement

def ft_min(series: pd.Series) -> float:
    """Calculate the minimum value of the series"""
    pass  # TODO: implement

def ft_max(series: pd.Series) -> float:
    """Calculate the maximum value of the series"""
    pass  # TODO: implement

def ft_percentile(series: pd.Series, p: float) -> float:
    """Calculate the p-th percentile of the series"""
    pass  # TODO: implement
