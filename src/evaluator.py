from sklearn.metrics import accuracy_score, classification_report
import streamlit as st

class Evaluator:
    @staticmethod
    def evaluate_model(y_test, y_pred):
        st.subheader("Model Evaluation")
        accuracy = accuracy_score(y_test, y_pred)
        st.write(f"Accuracy: {accuracy:.2f}")
        st.text("Classification Report:")
        st.text(classification_report(y_test, y_pred, zero_division=0))
