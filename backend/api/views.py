from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Dataset, Prediction
from .serializers import DatasetSerializer, PredictionSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from ml.model import make_predictions

#View for uploading datasets

class DatasetUploadView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        serializer = DatasetSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


#View for making predictions

class PredictionView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, dataset_id, *args, **kwargs):
        try:
            dataset = Dataset.objects.get(id=dataset_id)
            predictions = make_predictions(dataset.file.path) #Call ML model to generate predictions
            prediction_obj = Prediction.objects.create(dataset=dataset, predicted_value=predictions)
            serializer = PredictionSerializer(prediction_obj)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Dataset.DoesNoteExist:
            return Response ({"error": "Dataset not found"}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

