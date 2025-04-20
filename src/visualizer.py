import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

class Visualizer:
    @staticmethod
    def visualize_data(data):
        st.subheader("Feature Distributions")
        selected_feature = st.selectbox("Select a feature to visualize", data.columns[:-1])
        fig, ax = plt.subplots()
        sns.histplot(data[selected_feature], kde=True, ax=ax)
        st.pyplot(fig)

        st.subheader("Feature Correlations")
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.heatmap(data.corr(), annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig)
