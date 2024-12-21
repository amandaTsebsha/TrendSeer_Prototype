from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

from dashboard.app import response


# from .models import HistoricalData

def test_data_uploat(self):
    url = reverse('upload_data')
    data = {
        'name': 'New Data',
        'description': 'Test data upload',
        'data_file': 'path/to/file.csv',

    }
    response = self.client.post(url, data, format='multipart')
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)

def test_prediction(self):
    url = reverse('make_prediction', args=[self.historical_data.id])
    response = self.client.post(url)
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertIn('result', response.data)
