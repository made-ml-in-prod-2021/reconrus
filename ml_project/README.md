Homework 1
==============================

Next instructions assume that your terminal's working directory is ml_project 

### Installation:
~~~
conda create -n vy_made_ml_in_production_hw1 python=3.9.2
conda activate vy_made_ml_in_production_hw1
pip install -e .
~~~

### Usage

Configure ml_project/configs/train_config and launch
~~~
python ml_project/train_pipeline.py
~~~

Similar for `predict_pipeline`. To get predictions modify predict_config.yaml file:

1) Set correct `data_path` that leads to your test set
2) Set `features_to_drop: []` if data file does not already have a target column

### Test:
~~~
pytest tests/
~~~
