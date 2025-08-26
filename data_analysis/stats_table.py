import pandas as pd
from .stats_functions import ft_count

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

        # TODO: Replace with custom functions
        # count_val  = len(series)
        count_val  = ft_count(series)
        mean_val   = None  # ft_mean(series)
        std_val    = None  # ft_std(series)
        min_val    = None  # ft_min(series)
        p25_val    = None  # ft_percentile(series, 0.25)
        p50_val    = None  # ft_percentile(series, 0.50)
        p75_val    = None  # ft_percentile(series, 0.75)
        max_val    = None  # ft_max(series)

        rows.append([
            count_val, mean_val, std_val,
            min_val, p25_val, p50_val, p75_val, max_val
        ])

    stats = pd.DataFrame(
        rows,
        index=columns_to_use,
        columns=['count','mean','std','min','P25','P50','P75','max']
    ).T

    return stats
