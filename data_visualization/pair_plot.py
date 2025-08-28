import streamlit as st
import plotly.express as px
from data_visualization import DataVisualization

def show_pair_plot(df):
    st.markdown("### ❓ Pair plot of Hogwarts subjects")

    subjects = DataVisualization.get_subjects()

    st.markdown(
        "This scatter plot matrix shows all pairwise relationships between subjects. "
        "Use it to detect correlations, clusters, or separations between Hogwarts Houses. "
        "From this visualization, you can decide which features to use for logistic regression."
    )

    # --- Interactive scatter matrix ---
    fig = px.scatter_matrix(
        df,
        dimensions=subjects,
        color="Hogwarts House",
        color_discrete_map=DataVisualization.get_house_colors(),
        opacity=0.7,
        title="Hogwarts Subjects Pair Plot",
    )

    # Optional: adjust layout for readability
    fig.update_layout(
        height=1000, width=1000,
        dragmode='select',  # allows zooming and selection
        hovermode='closest'
    )

    st.plotly_chart(fig, use_container_width=True)
