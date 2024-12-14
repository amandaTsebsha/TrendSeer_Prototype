from rest_framework import serializers
from .models import Dataset, Prediction

#Dataset model serializer

class DatasetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dataset
        fields = ['id', 'name', 'file', 'upload_at']



    # def is_valid(self):
    #     pass
    #
    # def save(self):
    #     pass


class PredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prediction
        fields = ['id', 'dataset', 'predicted_value', 'predicted_at']
    # pass