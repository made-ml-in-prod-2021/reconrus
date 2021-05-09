import hydra
import numpy as np
import pickle

from ml_project.data.process_data import process_data
from ml_project.entities.prediction_params import PredictionParams
from ml_project.models.predict import predict
from ml_project.utils.logger import logger, setup_logger
from ml_project.utils.read_files import read_csv


def load_model(model_path: str):
    logger.debug(f'Started model loading from {model_path}')
    with open(model_path, 'rb') as fin:
        model = pickle.load(fin)
    logger.debug(f'Loaded model from {model_path}')
    return model


@hydra.main(config_path='configs', config_name='predict_config')
def predict_pipeline(params: PredictionParams):    
    setup_logger(params.logging_config)

    data = read_csv(params.data_path)
    transformer = load_model(params.transformer_path)
    X, _, _, _= process_data(transformer, data, None)
    model = load_model(params.model_path)
    predictions = predict(model, X)
    X[params.output_column] = predictions
    X.to_csv(params.output_path)


if __name__=='__main__':
    predict_pipeline()
