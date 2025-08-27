import streamlit as st
from model.logistic_regression import OneVsAllClassifier
import pandas as pd
import numpy as np

columns_to_use = ['Herbology', 'Astronomy', 'Ancient Runes']

if 'df' in st.session_state:
    train, predict = st.tabs(["Train", "Predict"])

    df: pd.DataFrame = st.session_state.df

    model = OneVsAllClassifier()

    with train:
        if "model_trained" not in st.session_state:
            st.session_state.model_trained = False
        if not st.session_state.model_trained:
            if st.button("Train Model"):
                # X = df.drop(columns=['Hogwarts House','Index', 'First Name', 'Last Name', 'Birthday', 'Best Hand'])
                X = df[columns_to_use]
                y = df['Hogwarts House']
                
                # DEBUG: Check data before training
                st.write("**Training Data Check:**")
                st.write(f"X shape: {X.shape}, y shape: {y.shape}")
                st.write(f"X has NaN: {X.isnull().sum().sum()}")
                st.write(f"y has NaN: {y.isnull().sum()}")
                st.write(f"Houses: {y.unique()}")
                st.write(f"X range: min={X.min().min():.2f}, max={X.max().max():.2f}")
                
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
                # X_input = input_df.drop(columns=['Index', 'First Name', 'Last Name', 'Birthday', 'Best Hand', 'Hogwarts House'], errors='ignore')
                X_input = input_df[columns_to_use]
                
                # DEBUG: Check prediction data
                st.write("**Prediction Data Check:**")
                st.write(f"X_input shape: {X_input.shape}")
                st.write(f"X_input has NaN: {X_input.isnull().sum().sum()}")
                st.write(f"X_input range: min={X_input.min().min():.2f}, max={X_input.max().max():.2f}")
                
                probabilities = st.session_state.model.predict_proba(X_input.values)
                predictions = st.session_state.model.predict(X_input.values)
                
                # DEBUG: Check predictions
                st.write("**Prediction Results Check:**")
                st.write(f"Unique predictions: {np.unique(predictions)}")
                st.write(f"Prediction counts: {np.bincount([list(st.session_state.model.classes).index(p) for p in predictions])}")
                for house, probs in probabilities.items():
                    st.write(f"{house} probs: min={probs.min():.3f}, max={probs.max():.3f}, mean={probs.mean():.3f}")
                
                results_df = input_df.copy()
                results_df['Predicted House'] = predictions
                for house, probs in probabilities.items():
                    results_df[f'Prob_{house}'] = probs
                
                st.write(results_df)
        else:
            st.warning("Please train the model first on the Train tab.")

else:
    st.warning("Please upload a dataset on the Home page")