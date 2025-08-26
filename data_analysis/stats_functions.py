import pandas as pd
import math

def ft_std(series: pd.Series, mean: float, count_val: int) -> float:
    """Calculate the standard deviation of the series"""
    summand = 0
    for val in series:
        if pd.notna(val):  # ignore NaN / None
            summand += (val - mean)**2

    return math.sqrt(summand / count_val)


def ft_percentile(p: float, count: int) -> float:
    """Calculate the p-th percentile of the series"""
    return p * (count + 1)
