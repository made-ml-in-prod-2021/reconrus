from http import HTTPStatus

import flask
import hydra
from flask import Flask, request

from ml_project.entities.prediction_params import PredictionParams
from ml_project.predict import predict_labels
from ml_project.utils import load_model, setup_logger

app = Flask(__name__)

transformer = None
model = None


@app.route('/predict', methods=['POST'])
def predict():
    data = request.json['data']
    predictions = predict_labels(data, model, transformer)
    results = {'predictions': predictions}
    return flask.jsonify(results), HTTPStatus.OK


@hydra.main(config_path='configs', config_name='predict_config')
def main(params: PredictionParams):
    setup_logger(params.logging_config)
    global transformer, model
    transformer = load_model(params.transformer_path)
    model = load_model(params.model_path)
    app.run(host='0.0.0.0')


if __name__ == '__main__':
    main()
