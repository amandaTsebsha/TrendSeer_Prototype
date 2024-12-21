import streamlit as st
import pandas as pd
import requests
from django.http import JsonResponse
from django.shortcuts import render
import json
from io import StringIO
from .charts import plot_predictions


st.set_page_config(page_title="TrendSeer", layout="wide")
st.title('TrendSeer - Business Prediction Dashboard')
st.write("This is where you visualize your predictions ")

upload_file = st.file_uploader("Upload you dataset", type='csv')

if upload_file is not None:
    # Read the uploaded CSV file into DataFrame
    dataframe = pd.read_csv(upload_file)

    st.write("Preview dataset:", dataframe.head())

    #Send dataset to backend API
    files = {'file': upload_file.getvalue()}
    response = requests.post('http://localhost:8000/api/upload/',files=files)

    if response.status_code == 201:
        st.success("Dataset uploaded successfully!")

        #Make Predictions
        dataset_id = response.json()['id']
        prediction_response = requests.get(f'http://localhost:8000/api/predict/{dataset_id}/')

        if prediction_response.status_code == 200:
            predictions = prediction_response.json()
            st.write("Predictions:", predictions)

        else:
            st.error("Error in making predictions.")

    else:
        st.error("Error in uploading dataset.")


def dashboard_view(request):
    """
    Renders the main dashboard page.
    """
    context = {
        'title': 'Dashboard',
        'description': 'Welcome to TrendSeer Dashboard',
    }
    return render(request, 'dashboard.html', context)



def chart_data():
    print("Chart Data")

    # return None