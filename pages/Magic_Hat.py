import streamlit as st

train, predict = st.tabs(["Train", "Predict"])

with train:
    st.header("Train your model here")
    st.write("This is where you can train your machine learning model.")

with predict:
    st.header("Make predictions here")
    st.write("This is where you can use your trained model to make predictions.")