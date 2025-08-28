import pandas as pd

class DataVisualization:
    """
    - List of subject columns
    - Hogwarts house colors
    """

    # Whitelist of subject columns
    whitelist = [
        "Arithmancy",
        "Astronomy",
        "Herbology",
        "Defense Against the Dark Arts",
        "Divination",
        "Muggle Studies",
        "Ancient Runes",
        "History of Magic",
        "Transfiguration",
        "Potions",
        "Care of Magical Creatures",
        "Charms",
        "Flying"
    ]

    # Hogwarts house colors
    HOUSE_COLORS = {
        "Gryffindor": "#740001",  # Red
        "Hufflepuff": "#FFDB00",  # Yellow
        "Ravenclaw": "#222F5B",   # Dark Blue
        "Slytherin": "#1A472A"    # Dark Green
    }

    @classmethod
    def get_subjects(cls):
        """Return the list of subjects"""
        return cls.whitelist

    @classmethod
    def get_house_colors(cls):
        """Return the house colors dictionary"""
        return cls.HOUSE_COLORS

# Find the most or least correlated pairs of subjects
def find_correlated_pairs(df: pd.DataFrame, top_n=4, most=True):
    """
    Compute correlation matrix for subject columns
    and return the top or bottom N unique pairs.
    
    Parameters:
    - df: DataFrame with subject columns
    - top_n: number of pairs to return
    - most: True → return most correlated, False → least correlated
    """
    subjects = DataVisualization.get_subjects()
    corr_matrix = df[subjects].corr(method="pearson")

    # Flatten matrix
    corr_unstacked = corr_matrix.unstack().dropna()

    # Remove self-correlations
    corr_unstacked = corr_unstacked[corr_unstacked < 0.9999]

    # Keep only one of (A, B) or (B, A)
    corr_unstacked = corr_unstacked.reset_index()
    corr_unstacked.columns = ["Feature1", "Feature2", "Correlation"]
    corr_unstacked = corr_unstacked[corr_unstacked["Feature1"] < corr_unstacked["Feature2"]]

    # Sort by absolute correlation
    corr_unstacked["AbsCorrelation"] = corr_unstacked["Correlation"].abs()
    sorted_pairs = corr_unstacked.sort_values(
        "AbsCorrelation", ascending=not most
    ).head(top_n)

    return sorted_pairs