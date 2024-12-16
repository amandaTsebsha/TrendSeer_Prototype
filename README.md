TrendSeer

TrendSeer is a predictive analytics application that combines Django for backend API and database management with Streamlit for an interactive dashboard. This project also integrates machine learning for data-driven predictions, leveraging an SQLite database for storing results and sample datasets.

Project Structure

trendseer/
├── backend/                      # Django backend for API and database management
│   ├── manage.py                 # Django management script
│   ├── trendseer/                # Django project folder
│   │   ├── __init__.py
│   │   ├── settings.py           # Django settings
│   │   ├── urls.py               # Main URL routing for the backend
│   │   ├── wsgi.py
│   │   ├── asgi.py
│   ├── api/                      # API app for dataset handling and predictions
│   │   ├── __init__.py
│   │   ├── models.py             # Database models (Dataset, Prediction)
│   │   ├── views.py              # API views (upload and prediction logic)
│   │   ├── serializers.py        # Serialization for dataset handling
│   │   ├── urls.py               # API-specific routing (upload and predict)
│   │   ├── tasks.py              # Background tasks (optional)
│   │   ├── tests.py              # Tests for backend
├── ml/                           # Machine Learning pipeline and scripts
│   ├── model.py                  # ML model and prediction logic
│   ├── preprocess.py             # Data preprocessing steps
│   ├── train.py                  # Model training script
│   ├── requirements.txt          # ML-specific dependencies
├── dashboard/                    # Frontend using Streamlit
│   ├── app.py                    # Main Streamlit app
│   ├── charts.py                 # Helper functions for charts/visualizations
│   ├── styles.css                # CSS styling for Streamlit
├── data/                         # Data files
│   ├── sample_data.csv           # Example dataset for testing
│   ├── predictions.db            # SQLite database for storing predictions
├── tests/                        # Unit tests for various components
│   ├── test_api.py               # Tests for API endpoints
│   ├── test_ml.py                # Tests for ML pipeline
│   ├── test_dashboard.py         # Tests for frontend functionality
├── README.md                     # Project documentation
├── requirements.txt              # Project dependencies
└── .gitignore                    # Git ignore file (for avoiding unnecessary files)

Features

Streamlit Dashboard: Interactive dashboard for visualizing trends and predictions.

Django REST API: Provides endpoints for uploading data, running predictions, and retrieving results.

Machine Learning: Predictive model integration for data analytics.

SQLite Database: Lightweight storage solution for datasets and prediction results.

Custom Charts: Dynamic data visualization with support for user interactions.

Requirements

Python 3.8+

Django 5.1.4

Django REST Framework

Streamlit

Pandas

Matplotlib / Plotly

SQLite (default database)

Installation

Clone the Repository

git clone https://github.com/yourusername/TrendSeer.git
cd TrendSeer

Install Dependencies

Create a virtual environment and install the required packages:

python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
pip install -r requirements.txt

Install ML-specific dependencies:

pip install -r ml/requirements.txt

Usage

1. Start the Django Backend

Navigate to the backend/ directory and start the server:

cd backend
python manage.py migrate  # Apply database migrations
python manage.py runserver  # Start Django server

The backend API will be available at http://127.0.0.1:8000/.

2. Start the Streamlit Dashboard

Navigate to the dashboard/ directory and run the Streamlit app:

cd dashboard
streamlit run app.py

The dashboard will be available at http://localhost:8501.

API Endpoints

The Django backend provides the following endpoints:

Fetch Predictions

URL: /api/fetch-predictions/

Method: GET

Response: JSON list of predictions.

Submit Data

URL: /api/submit-data/

Method: POST

Payload:

{
  "date": "YYYY-MM-DD",
  "value": 100.0
}

Response: JSON object with the generated prediction.

Directory Details

Backend

The backend/ folder contains the Django application responsible for:

API endpoints (backend/api/urls.py, views.py)

Database management using SQLite (models.py)

Serialization of data (serializers.py)

ML

The ml/ folder contains the machine learning pipeline, including:

model.py: Predictive model logic.

preprocess.py: Preprocessing scripts for incoming data.

train.py: Model training scripts.

Dashboard

The dashboard/ folder is the frontend powered by Streamlit, responsible for:

Displaying data trends and predictions.

Fetching data from the API via requests.

Submitting user-provided data for predictions.

Example Workflow

Start the Django server and Streamlit dashboard.

Upload a dataset via the dashboard.

The backend API processes the data, makes predictions using the ML model, and stores results in SQLite.

View predictions and trends on the dashboard.

Tests

Run tests for each module:

Backend Tests

cd backend
python manage.py test

ML Tests

pytest ml/

Dashboard Tests

pytest tests/test_dashboard.py

License

This project is licensed under the MIT License. See the LICENSE file for details.

Contributing

Contributions are welcome! To contribute:

Fork the repository.

Create a new branch for your feature or bugfix.

Submit a pull request with a detailed explanation of changes.

Authors

Amanda Nolwazi Tsebesha - https://github.com/amandaTsebsha


Acknowledgments

Special thanks to the open-source libraries and tools that made this project possible, including Django, Streamlit, and Python.

