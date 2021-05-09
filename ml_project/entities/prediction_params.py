from dataclasses import dataclass


@dataclass()
class PredictionParams:
    model_path: str
    data_path: str
    output_path: str
    output_column: str
    logging_config: str
    transformer_path: str
