import streamlit as st
import plotly.express as px
from data_visualization import DataVisualization

def show_histogram(df):
    question = "Which Hogwarts course has a homogeneous score distribution between all four houses?"
    st.markdown(f"### ❓ {question}")

    # Use the class methods
    subject = st.selectbox("Select a course", DataVisualization.get_subjects())

    fig = px.histogram(
        df,
        x=subject,
        color="Hogwarts House",
        barmode="overlay",
        opacity=0.6,
        nbins=30,
        title=f"Distribution of {subject} Scores by House",
        color_discrete_map=DataVisualization.get_house_colors()
    )

    st.plotly_chart(fig, use_container_width=True)
