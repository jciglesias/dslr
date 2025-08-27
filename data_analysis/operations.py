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

def operations(series: pd.Series) -> list:
    count_val  = 0
    mean_val   = 0  # ft_mean(series)
    first_value = True
    for val in series:
        if pd.notna(val):  # ignore NaN / None

            # Count
            count_val += 1

            # Min, Max
            if first_value == True:
                min_val, max_val = val, val
                first_value = False

            if min_val > val:
                min_val = val

            if max_val < val:
                max_val = val

            # Mean
            mean_val += val
            
    if mean_val != 0:
        mean_val = mean_val / count_val

    std_val    = ft_std(series, mean_val, count_val)
    p25_val    = ft_percentile(0.25, count_val)
    p50_val    = ft_percentile(0.50, count_val)
    p75_val    = ft_percentile(0.75, count_val)
    
    return [count_val, mean_val, std_val,
            min_val, p25_val, p50_val, p75_val, max_val]