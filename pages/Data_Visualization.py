import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.datasets import make_blobs

histogram, scatter, pair = st.tabs(["Histogram", "Scatter Plot", "Pair Plot"])

with histogram:
    question = 'Which Hogwarts course has a homogeneous score distribution between all four houses?'

    tmp_data = pd.DataFrame({
        'Hogwarts Course': ['Astronomy', 'Herbology', 'History of Magic', 'Defense Against the Dark Arts', 'Divination', 'Muggle Studies', 'Potions'],
        'House Slytherin': [3, 2, 4, 5, 1, 2, 3],
        'House Gryffindor': [4, 3, 5, 2, 4, 3, 4],
        'House Ravenclaw': [5, 4, 3, 4, 5, 4, 5],
        'House Hufflepuff': [2, 5, 2, 3, 2, 5, 2]
    })

    st.write(question)
    fig = px.histogram(tmp_data, x='Hogwarts Course', y=['House Slytherin', 'House Gryffindor', 'House Ravenclaw', 'House Hufflepuff'], barmode='group', title='Score Distribution by Hogwarts Course and House')
    st.plotly_chart(fig)

with scatter:
    question = 'What are the two features that are similar?'

    tmp_data = pd.DataFrame({
        'Feature1': [10, 20, 30, 40, 50, 60, 70],
        'Feature2': [12, 22, 32, 42, 52, 62, 72],
        'Feature3': [50, 40, 30, 20, 10, 0, -10],
    })

    st.write(question)
    X, y = make_blobs(n_samples=100, centers=3, n_features=2, random_state=42)
    df = pd.DataFrame(X, columns=['Feature A', 'Feature B'])
    df['Cluster'] = y
    fig = px.scatter(df, x='Feature A', y='Feature B', color='Cluster', title='Scatter Plot of Features A and B with Clusters')
    st.plotly_chart(fig)

with pair:
    st.header("Pair Plot")
    st.write("This is where you can create a pair plot.")
