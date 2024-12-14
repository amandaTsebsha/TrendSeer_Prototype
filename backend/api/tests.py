from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Dataset, Prediction

class DatasetUploadTest(APITestCase):
    def test_upload_dataset(self):
        url = reverse('upload-dataset')
        data = {'name': 'Test Dataset', 'file': open('path_to_sample_data.csv', 'rb')}
        response = self.client.post(url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class PredictionTest(APITestCase):
    def test_make_prediction(self):
        dataset = Dataset.objects.create(name='Test Dataset', file='path_to_sample_data.csv')
        url = reverse('make-prediction', args=[dataset.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual('predicted_value', response.data)