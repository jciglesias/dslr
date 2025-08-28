import streamlit as st
import plotly.express as px
from data_visualization import DataVisualization

SUBJECT_ABBREVIATIONS = {
    "Arithmancy": "Arithm.",
    "Astronomy": "Astro.",
    "Herbology": "Herb.",
    "Defense Against the Dark Arts": "Def. Arts",
    "Divination": "Divin.",
    "Muggle Studies": "Mug. Stud",
    "Ancient Runes": "Anc. Runes",
    "History of Magic": "Hist. Magic",
    "Transfiguration": "Transfig",
    "Care of Magical Creatures": "Care Creat."
}

def show_pair_plot(df):
    st.markdown("### ❓ Pair plot of Hogwarts subjects")
    st.markdown(
        "This scatter plot matrix shows all pairwise relationships between subjects. "
        "Use it to detect correlations, clusters, or separations between Hogwarts Houses. "
        "From this visualization, you can decide which features to use for logistic regression."
    )

    subjects = DataVisualization.get_subjects()
    labels = {s: SUBJECT_ABBREVIATIONS.get(s, s) for s in subjects}

    # --- Interactive scatter matrix ---
    fig = px.scatter_matrix(
        df,
        dimensions=subjects,  # Use original column names for data
        color="Hogwarts House",
        color_discrete_map=DataVisualization.get_house_colors(),
        opacity=0.7,
        labels=labels,        # Handles the displayed axis names
        title="Hogwarts Subjects Pair Plot"
    )

    # Adjust layout for readability
    fig.update_layout(
        height=1000,
        width=1000,
        dragmode='select', # Allows zooming and selection
        hovermode='closest',
        font=dict(size=10)
    )

    st.plotly_chart(fig, use_container_width=True)
