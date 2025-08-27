import streamlit as st
import plotly.express as px
from data_visualization import DataVisualization

def find_top_correlated(df, top_n=3):
    """
    Compute correlation matrix for subject columns
    and return the top N unique pairs with the highest absolute correlation.
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
    top_pairs = corr_unstacked.sort_values("AbsCorrelation", ascending=False).head(top_n)

    return top_pairs

def show_scatter_plot(df):
    question = "What are the two features that are similar?"
    st.markdown(f"### ❓ {question}")

    subjects = DataVisualization.get_subjects()

    # --- Auto-detect top correlated pairs ---
    top_pairs = find_top_correlated(df, top_n=3)

    st.markdown("**Top correlated feature pairs (auto-detected):**")
    for _, row in top_pairs.iterrows():
        feat1, feat2, corr = row["Feature1"], row["Feature2"], row["Correlation"]
        st.markdown(f"- `{feat1}` vs `{feat2}` (correlation = {corr:.2f})")

        fig = px.scatter(
            df,
            x=feat1,
            y=feat2,
            color="Hogwarts House",
            color_discrete_map=DataVisualization.get_house_colors(),
            title=f"Scatter plot: {feat1} vs {feat2} (corr={corr:.2f})",
            opacity=0.7,
        )
        st.plotly_chart(fig, use_container_width=True)

    # --- Allow manual exploration ---
    st.markdown("### 🔎 Explore other pairs")
    x_subject = st.selectbox("Select X-axis subject", subjects, index=0)
    y_subject = st.selectbox("Select Y-axis subject", subjects, index=1)

    if x_subject != y_subject:
        fig_custom = px.scatter(
            df,
            x=x_subject,
            y=y_subject,
            color="Hogwarts House",
            color_discrete_map=DataVisualization.get_house_colors(),
            title=f"Scatter plot of {x_subject} vs {y_subject}",
            opacity=0.7,
        )
        st.plotly_chart(fig_custom, use_container_width=True)
