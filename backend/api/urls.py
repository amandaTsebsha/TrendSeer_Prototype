from django.urls import path
from .views import DatasetUploadView, PredictionView

urlpatterns = [
    path('upload/', DatasetUploadView.as_view(), name='upload-dataset'),
    path('predict/<int:dataset_id>/', PredictionView.as_view(), name='make-prediction'),
]