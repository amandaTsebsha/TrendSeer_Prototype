from django.contrib import admin
from django.urls import path, include

from backend.api.views import DatasetUploadView, PredictionView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Include routes from the 'api' app
]

apiUrlpatterns = [
    path('upload/', DatasetUploadView.as_view(), name='upload-dataset'),
    path('predict/<int:dataset_id>/', PredictionView.as_view(), name='make-prediction'),
]
