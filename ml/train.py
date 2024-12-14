from ml.preprocess import preprocess_data
from ml.model import train_model

def train():

    # Path to dataset
    dataset_path = 'data/sample_data.csv'

    processed_data = preprocess_data(dataset_path)

    train_model(dataset_path)

    if __name__ == "__main__":
        train()


