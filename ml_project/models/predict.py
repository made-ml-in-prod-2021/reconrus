import numpy as np
import pandas as pd
import pickle

from ml_project.entities.prediction_params import PredictionParams
from ml_project.utils.logger import logger
from ml_project.utils.read_files import read_csv


def predict(model, X: pd.DataFrame) -> np.array:
    logger.debug(f'Started prediction')
    y = model.predict(X)
    logger.debug(f'Finished prediction')
    return y
