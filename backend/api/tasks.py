from celery import shared_task
from ml.model import make_predictions
from .models import Dataset, Prediction


@shared_task
def generate_prediction(dataset_id):
    try:
        dataset = Dataset.objects.get(id=dataset_id)
        predictions = make_predictions(dataset.file.path) #Call ML to generate predictions
        prediction_obj = Prediction.objects.create(dataset=dataset, predicted_value=predictions)

    except Dataset.DoesNotExist:
        pass #Handle exception if dataset doesn't exist

    except Exception as e:
        print(f"Error: {e}")

