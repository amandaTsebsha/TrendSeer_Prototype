import pickle
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

#Fucntion to train model

def train_model(dataset_path):
    # Load the dataset (assuming it's a CSV file)
    data = pd.read_csv(dataset_path)
    #Assume the last column id the target varialble

    X = data.iloc[:, :-1] #Features
    Y = data.iloc[:, :-1] #Target

    #Split into testing and training sets

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    #Inititalize the model
    model = RandomForestRegressor(n_estimators=100, random_state=42)

    #Train Model
    model.fit(X_train, Y_train)

    #Prediction on test set
    y_pred = model.predict(X_test)

    #Calculate and print perfomance
    mse = mean_squared_error(Y_test, y_pred)
    print(f'Mean Squared Error: {mse}')

    #Save trained model
    with open('ml_model.pkl', 'wb') as model_file:
        pickle.dump(model, model_file)
        print("Model trained, saved as ml_model.pkl")


def make_predictions(dataset_path):
    #Load trained data
    with open('ml_model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)

        #Load data to predict
        data = pd.read_csv(dataset_path)

        X = data.iloc[:, :-1]

        predcitions = model.predict(X)
        return predcitions
