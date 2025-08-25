import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.datasets import make_blobs

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