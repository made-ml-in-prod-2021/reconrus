import logging
import yaml

logger = logging.getLogger(__name__)

def setup_logger(configuration_path):
    with open(configuration_path) as config_fin:
        logging.config.dictConfig(yaml.safe_load(config_fin))
