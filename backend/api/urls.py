from django.urls import path
from .views import DatasetUploadView, PredictionView
from dashboard import app

urlpatterns = [
    path('upload/', DatasetUploadView.as_view(), name='upload-dataset'),
    path('predict/<int:dataset_id>/', PredictionView.as_view(), name='make-prediction'),
]

urlpattern = [
    path("", app.dashboard_view, name="dashboard"),
    path("chart-data/", app.chart_data, name="chart-data"),
]