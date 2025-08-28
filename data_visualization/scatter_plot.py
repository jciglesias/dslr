import streamlit as st
import plotly.express as px
from data_visualization import DataVisualization, find_correlated_pairs

def plot_correlation_pairs(df, pairs_df, title="Correlation pairs", height=300):
    st.markdown(f"**{title}**")

    for i in range(0, len(pairs_df), 2):
        cols = st.columns(2)
        for j in range(2):
            if i + j < len(pairs_df):
                row = pairs_df.iloc[i + j]
                feat1, feat2, corr = row["Feature1"], row["Feature2"], row["Correlation"]

                with cols[j]:
                    st.markdown(f"**{feat1} vs {feat2}**  \n(corr = {corr:.2f})")
                    fig = px.scatter(
                        df,
                        x=feat1,
                        y=feat2,
                        color="Hogwarts House",
                        color_discrete_map=DataVisualization.get_house_colors(),
                        opacity=0.7,
                    )
                    fig.update_layout(height=height)
                    st.plotly_chart(fig, width='stretch')

def show_scatter_plot(df):
    question = "What are the two features that are similar?"
    st.markdown(f"### ❓ {question}")

    subjects = DataVisualization.get_subjects()

    # --- Auto-detect: Top most similar (positive correlation) ---
    top_similar = find_correlated_pairs(df, top_n=4, sign="positive")
    plot_correlation_pairs(df, top_similar, title="Most similar feature pair")

    # --- Auto-detect: Top most different (negative correlation) ---
    most_different = find_correlated_pairs(df, top_n=4, sign="negative")
    plot_correlation_pairs(df, most_different, title="Most opposite feature pair")

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
        st.plotly_chart(fig_custom, width='stretch')
