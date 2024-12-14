import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

#Processing dataset
def preprocess_data(dataset_path):

    data = pd.read_csv(dataset_path)

    #Identify numeric and categorical columns
    numeric_cols = data.select_dtypes(include=['float64', 'int64']).columns
    categorical_cols = data.select_dtypes(include=['object']).columns

    #Preprocessing pipeline
    numeric_tranformer = Pipeline(steps=[('imputer', SimpleImputer(strategy='mean')),
                                         ('scaler', StandardScaler())])
    categorical_tranfromer = Pipeline(steps=[('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
                                             ('onehot', OneHotEncoder(handle_unknown='ignore'))])
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_tranformer, numeric_cols), ('cat', categorical_tranfromer, categorical_cols)])

    #Apply Preprocessing transfformations to the dataset
    processed_data = preprocessor.fit_transform(data)
    return processed_data