import matplotlib.pyplot as plt
import plotly.graph_objects as go
import seaborn as sns
import streamlit as st
import pandas as pd

#Function to create bar chart

def plot_predictions(predictions):
    # Create a DataFrame from the predictions
    df = pd.DataFrame(predictions, columns=["Predicted Value"])

    # Create a Plotly bar chart
    fig = go.Figure()

    # Add a bar trace for the predicted values
    fig.add_trace(go.Bar(x=df.index, y=df["Predicted Value"], name="Predicted Value", marker_color='skyblue'))

    #Update layout for better styling
    fig.update_layout(title="Predicted Values", xaxis_title="Index", yaxis_title="Predicted Values",
                      template='plotly_dark', height=600, width=800)

    st.plotly_chart(fig)


def plot(predictions):
    plt.figure(figsize=(10, 6))
    plt.plot(predictions)
    plt.title('Prediction Results Over Time')
    plt.xlabel('Time')
    plt.ylabel('Prediction Value')
    plt.grid(True)
    plt.show()