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

Similar for `predict_pipeline`

Test:
~~~
pytest tests/
~~~
