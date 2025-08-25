import streamlit as st
import pandas as pd
import plotly.express as px

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