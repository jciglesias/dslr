import pandas as pd

def stats_table(df: pd.DataFrame) -> pd.DataFrame:
    rows = []

    for col in df.columns:
        series = df[col]

        # TODO: Replace with custom functions
        count_val  = len(series)
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
        index=df.columns,
        columns=['count','mean','std','min','P25','P50','P75','max']
    ).T

    return stats
