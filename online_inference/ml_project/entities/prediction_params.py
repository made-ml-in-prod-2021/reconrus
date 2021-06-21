from dataclasses import dataclass


@dataclass()
class PredictionParams:
    model_path: str
    logging_config: str
    transformer_path: str
