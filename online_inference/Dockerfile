FROM python:3.8
COPY . /online_inference
WORKDIR /online_inference
RUN pip install -e .

EXPOSE 5000
CMD ["python3", "ml_project/app.py"]
