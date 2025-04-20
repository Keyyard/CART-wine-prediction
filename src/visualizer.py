import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from abc import ABC, abstractmethod

class VisualizationStrategy(ABC): #interface class
    @abstractmethod
    def visualize(self, data):
        pass

class DistributionChart(VisualizationStrategy):
    def visualize(self, data):
        selected_feature = st.selectbox("Select a feature to visualize", data.columns[:-1])
        fig, ax = plt.subplots()
        sns.histplot(data[selected_feature], kde=True, ax=ax)
        st.pyplot(fig)

class Heatmap(VisualizationStrategy):
    def visualize(self, data):
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.heatmap(data.corr(), annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig)

class BoxPlot(VisualizationStrategy):
    def visualize(self, data):
        selected_feature = st.selectbox("Select a feature to visualize", data.columns[:-1])
        fig, ax = plt.subplots()
        sns.boxplot(x=data[selected_feature], ax=ax)
        st.pyplot(fig)

class ScatterPlot(VisualizationStrategy):
    def visualize(self, data):
        feature_x = st.selectbox("Select X-axis feature", data.columns[:-1])
        feature_y = st.selectbox("Select Y-axis feature", data.columns[:-1])
        fig, ax = plt.subplots()
        sns.scatterplot(x=data[feature_x], y=data[feature_y], ax=ax)
        st.pyplot(fig)

class PairPlot(VisualizationStrategy):
    def visualize(self, data):
        st.write("Generating pair plot for all features...")
        fig = sns.pairplot(data)
        st.pyplot(fig)

class LinePlot(VisualizationStrategy):
    def visualize(self, data):
        feature_x = st.selectbox("Select X-axis feature", data.columns[:-1])
        feature_y = st.selectbox("Select Y-axis feature", data.columns[:-1])
        fig, ax = plt.subplots()
        sns.lineplot(x=data[feature_x], y=data[feature_y], ax=ax)
        st.pyplot(fig)

class ViolinPlot(VisualizationStrategy):
    def visualize(self, data):
        selected_feature = st.selectbox("Select a feature to visualize", data.columns[:-1])
        fig, ax = plt.subplots()
        sns.violinplot(x=data[selected_feature], ax=ax)
        st.pyplot(fig)

class BarPlot(VisualizationStrategy):
    def visualize(self, data):
        selected_feature = st.selectbox("Select a feature to visualize", data.columns[:-1])
        fig, ax = plt.subplots()
        sns.barplot(x=data[selected_feature].value_counts().index, y=data[selected_feature].value_counts().values, ax=ax)
        st.pyplot(fig)

class SwarmPlot(VisualizationStrategy):
    def visualize(self, data):
        selected_feature = st.selectbox("Select a feature to visualize", data.columns[:-1])
        fig, ax = plt.subplots()
        sns.swarmplot(x=data[selected_feature], ax=ax)
        st.pyplot(fig)

class StripPlot(VisualizationStrategy):
    def visualize(self, data):
        selected_feature = st.selectbox("Select a feature to visualize", data.columns[:-1])
        fig, ax = plt.subplots()
        sns.stripplot(x=data[selected_feature], ax=ax)
        st.pyplot(fig)

class Visualizer:
    def __init__(self):
        self.strategies = {
            "Distribution Chart": DistributionChart(),
            "Heatmap": Heatmap(),
            "Box Plot": BoxPlot(),
            "Scatter Plot": ScatterPlot(),
            "Pair Plot": PairPlot(),
            "Line Plot": LinePlot(),
            "Violin Plot": ViolinPlot(),
            "Bar Plot": BarPlot(),
            "Swarm Plot": SwarmPlot(),
            "Strip Plot": StripPlot()
        }

    def visualize_data(self, data):
        st.subheader("Data Visualization")
        chart_type = st.selectbox("Select a chart type to visualize", list(self.strategies.keys()))
        strategy = self.strategies[chart_type]
        strategy.visualize(data)
