import logging
from typing import List, Optional

import pandas as pd

from ml_project.features.build_features import OneHotTransformer


def predict_labels(data_json, model, transformer) -> List[int]:
    data = pd.DataFrame(data_json)
    logging.debug(f'Processing data')
    processed_data, _ = transformer.transform(data, None)
    logging.debug(f'Finished processing')

    logging.debug(f'Started prediction')
    y = model.predict(processed_data)
    logging.debug(f'Finished prediction')
    return y.tolist()
