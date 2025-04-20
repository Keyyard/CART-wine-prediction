import pandas as pd
import streamlit as st
import random

class UserInputPredictor:
    @staticmethod
    def get_user_input(features):
        user_input = {}
        for feature in features:
            user_input[feature] = st.number_input(f"Enter {feature}", value=random.uniform(0, 10), step=0.1)
        return pd.DataFrame([user_input])

    @staticmethod
    def predict_quality(model, user_input_df):
        if st.button("Predict Quality"):
            prediction = model.predict(user_input_df)
            label = "Good" if prediction[0] >= 5 else "Bad"
            st.write(f"Predicted Wine Quality: {prediction[0]} (Label: {label})")
