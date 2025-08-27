import streamlit as st
from model.logistic_regression import OneVsAllClassifier
import pandas as pd
import numpy as np

columns_to_use = ['Herbology', 'Astronomy', 'Ancient Runes', 'Charms', 'Defense Against the Dark Arts']

if 'df' in st.session_state:
    train, predict = st.tabs(["Train", "Predict"])

    df: pd.DataFrame = st.session_state.df

    model = OneVsAllClassifier()

    with train:
        if "model_trained" not in st.session_state:
            st.session_state.model_trained = False
        if not st.session_state.model_trained:
            if st.button("Train Model"):
                X = df[columns_to_use]
                y = df['Hogwarts House']
                
                model.fit(X.values, y.values)
                st.session_state.model_trained = True
                st.session_state.model = model
                st.success("Model trained successfully!")
        else:
            st.success("Model is already trained.")

    with predict:
        if st.session_state.model_trained:
            st.write("Upload a CSV file with the same features as the training data (excluding 'Hogwarts House').")
            uploaded_file = st.file_uploader("Choose a file", type="csv")
            if uploaded_file is not None:
                input_df = pd.read_csv(uploaded_file)
                X_input = input_df[columns_to_use]
 
                probabilities = st.session_state.model.predict_proba(X_input.values)
                predictions = st.session_state.model.predict(X_input.values)
                
                results_df = input_df.copy()
                results_df['Predicted House'] = predictions
                for house, probs in probabilities.items():
                    results_df[f'Prob_{house}'] = probs
                
                st.write(results_df)
        else:
            st.warning("Please train the model first on the Train tab.")

else:
    st.warning("Please upload a dataset on the Home page")