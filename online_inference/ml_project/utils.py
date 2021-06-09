import logging
import yaml

import pickle


def load_model(model_path: str):
    logging.debug(f'Started model loading from {model_path}')
    with open(model_path, 'rb') as fin:
        model = pickle.load(fin)
    logging.debug(f'Loaded model from {model_path}')
    return model


def setup_logger(configuration_path):
    with open(configuration_path) as config_fin:
        logging.config.dictConfig(yaml.safe_load(config_fin))
    logging.debug('Configured logger')
