### Docker

In this repository launch: `sudo docker build -t reconrus/made-ml-prod-hw2:v1 .`
To run the image: `sudo docker run reconrus/made-ml-prod-hw2:v1`

To pull the image: `sudo docker pull  reconrus/made-ml-prod-hw2:v1`

### Request

`python3 ml_project/send_request.py [PATH_TO_CSV_DATA] [SERVER_IP] [SERVER_PORT]

### Self-assessment

1) Оберните inference вашей модели в rest сервис(вы можете использовать как FastAPI, так и flask, другие желательно не использовать, дабы не плодить излишнего разнообразия для проверяющих), должен быть endpoint /predict (3 балла)   
   **+3 балла**
2) Напишите тест для /predict  (3 балла) (https://fastapi.tiangolo.com/tutorial/testing/, https://flask.palletsprojects.com/en/1.1.x/testing/)
   **+0 баллов**
3) Напишите скрипт, который будет делать запросы к вашему сервису -- 2 балла
   ml_project/send_request.py **+2 балла**
4) **+0 баллов**
5) Напишите dockerfile, соберите на его основе образ и запустите локально контейнер(docker build, docker run), внутри контейнера должен запускать сервис, написанный в предущем пункте, закоммитьте его, напишите в readme корректную команду сборки (4 балл)
   **+4 балла**
6) **+0 баллов**
7) опубликуйте образ в https://hub.docker.com/, используя docker push (вам потребуется зарегистрироваться) (2 балла)
   **+2 балла** https://hub.docker.com/repository/docker/reconrus/made-ml-prod-hw2
8) напишите в readme корректные команды docker pull/run, которые должны привести к тому, что локально поднимется на inference ваша модель (1 балл)
   **+1 балл**
9) проведите самооценку -- 1 доп балл
   **+1 балл**
