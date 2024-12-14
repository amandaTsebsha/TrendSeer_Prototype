from django.db import models

#Model for storing upload datasets

class Dataset(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='datasets/')
    upload_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

#Models for storing predictions made bt the ML Model

class Prediction(models.Model):
    dataset = models.ForeignKey(Dataset, related_name='predictions', on_delete=models.CASCADE)
    predicted_value = models.FloatField()
    predicted_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Prediction for {self.dataset.name} at {self.predicted_at}"
