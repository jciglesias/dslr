import pandas as pd
from .stats_functions import ft_std, ft_percentile

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

def stats_table(df: pd.DataFrame, whitelist=None) -> pd.DataFrame:
    """
    df: pandas DataFrame to analyze
    whitelist: list of column names to include. If None, use all columns.
    """
    # Determine which columns to use
    if whitelist is None:
        columns_to_use = df.columns
    else:
        # Keep only columns that exist in df
        columns_to_use = [col for col in whitelist if col in df.columns]

    rows = []

    for col in columns_to_use:
        series = df[col]
        rows.append(operations(series))

    stats = pd.DataFrame(
        rows,
        index=columns_to_use,
        columns=['count','mean','std','min','P25','P50','P75','max']
    ).T

    return stats
