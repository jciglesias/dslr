import streamlit as st
import plotly.express as px
from data_visualization import DataVisualization

def show_histogram(df):
    question = "Which Hogwarts course has a homogeneous score distribution between all four houses?"
    st.markdown(f"### ❓ {question}")

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

    # === Grid version of all the subjects ===
    st.markdown("### 📊 All courses")

    subjects = DataVisualization.get_subjects()

    # Two per row
    for i in range(0, len(subjects), 2):
        cols = st.columns(2)
        for j, col in enumerate(cols):
            if i + j < len(subjects):
                subj = subjects[i + j]
                with col:
                    st.markdown(f"**{subj}**")
                    fig = px.histogram(
                        df,
                        x=subj,
                        color="Hogwarts House",
                        barmode="overlay",
                        opacity=0.6,
                        nbins=30,
                        color_discrete_map=DataVisualization.get_house_colors()
                    )
                    fig.update_layout(height=300)
                    st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})
