import streamlit as st
from sklearn.model_selection import train_test_split
import pandas as pd

from src.data_loader import DataLoader
from src.visualizer import Visualizer
from src.model_trainer import ModelTrainer
from src.evaluator import Evaluator
from src.comparison_table import ComparisonTable
from src.predictor import Predictor

import config

def run():
    st.title("Wine Quality Prediction")

    # load data
    st.header("Data Overview")
    data = DataLoader.load_data()
    st.subheader("Dataset Preview")
    st.write(data.head())
    st.subheader("Basic Statistics")
    st.write(data.describe())

    # visualize
    visualizer = Visualizer()
    visualizer.visualize_data(data)

    # split data to sets (80% train, 20% test)
    X = data.drop('quality', axis=1)
    y = data['quality']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # train with user input depth
    st.header("Model Training")
    st.subheader("Train the CART Model")
    max_depth = st.slider("Select max depth for the tree", min_value=1, max_value=20, value=5)
    model = ModelTrainer.train_model(X_train, y_train, max_depth)
    st.write("Model trained successfully!")

    # predicts
    st.subheader("Model Predictions")
    predictions_df, y_pred = Predictor.make_predictions(model, X_test)
    st.write(predictions_df.head(10))

    # create tables
    st.subheader("Comparison Table")
    comparison_df = ComparisonTable.create_comparison_table(y_test, y_pred)
    ComparisonTable.display_comparison_table(comparison_df)

    # evaluate model performance 
    st.header("Model Evaluation")
    Evaluator.evaluate_model(y_test, y_pred)
    
    # footer
    st.markdown(""" 
    --- 
    *By Keyyard - Trinh Minh Hieu* 
    """)