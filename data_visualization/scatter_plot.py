import streamlit as st
import plotly.express as px
from data_visualization import DataVisualization

def show_scatter_plot(df):
    question = "What are the two features that are similar?"
    st.markdown(f"### ❓ {question}")

    subjects = DataVisualization.get_subjects()

    # Pick X and Y
    x_subject = st.selectbox("Select X-axis subject", subjects, index=0)
    y_subject = st.selectbox("Select Y-axis subject", subjects, index=1)

    # Scatter plot colored by House
    fig = px.scatter(
        df,
        x=x_subject,
        y=y_subject,
        color="Hogwarts House",
        color_discrete_map=DataVisualization.get_house_colors(),
        title=f"Scatter plot of {x_subject} vs {y_subject}",
        opacity=0.7
    )

    st.plotly_chart(fig, use_container_width=True)
