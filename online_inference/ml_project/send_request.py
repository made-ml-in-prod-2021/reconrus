import requests
from http import HTTPStatus

import click
import pandas as pd


def read_data(path: str):
    df = pd.read_csv(path)
    df = df.drop('target', axis=1)
    data = df.to_dict(orient='records')
    return data

@click.command()
@click.argument('data_path')
@click.argument('ip', type=str)
@click.argument('port', type=str)
def main(data_path: str, ip: str, port: str):
    url = f'http://{ip}:{port}/predict'
    data = read_data(data_path)
    response = requests.post(url, json={'data': data})
    if response.status_code == HTTPStatus.OK:
        print(f'response: {response.json()}')


if __name__=='__main__':
    main()
