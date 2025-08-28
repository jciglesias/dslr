import pandas as pd
import math

def ft_std(series: pd.Series, mean: float, count_val: int) -> float:
    """Calculate the standard deviation of the series"""
    summand = 0
    for val in series:
        if pd.notna(val):  # ignore NaN / None
            summand += (val - mean)**2

    return math.sqrt(summand / count_val)


def ft_percentile(series: pd.Series, p: float, count: int) -> float:
    """Calculate the p-th percentile of the series"""
    if p < 0 or p > 1 or count == 0:
        return None

    sorted_series = sorted([val for val in series if pd.notna(val)])
    rank = p * (count + 1)

    if rank < 1:
        return sorted_series[0]
    elif rank >= count:
        return sorted_series[-1]
    
    lower_index = int(rank) - 1
    upper_index = min(lower_index + 1, count - 1)
    fraction = rank - (lower_index + 1)
    
    lower_value = sorted_series[lower_index]
    upper_value = sorted_series[upper_index]

    return lower_value + fraction * (upper_value - lower_value)

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
    p25_val    = ft_percentile(series, 0.25, count_val)
    p50_val    = ft_percentile(series, 0.50, count_val)
    p75_val    = ft_percentile(series, 0.75, count_val)
    
    return [count_val, mean_val, std_val,
            min_val, p25_val, p50_val, p75_val, max_val]