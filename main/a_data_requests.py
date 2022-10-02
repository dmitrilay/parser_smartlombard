import json
import requests
from requests.auth import AuthBase
from settings import *


class TokenAuth(AuthBase):
    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        r.headers['X-TokenAuth'] = f'{self.token}'
        return r


def sending_spec(obj=0):
    if obj:
        pathname = PATH_NAME
        host = HOST
        url = f'{host}{pathname}'

        _json = json.dumps(obj)
        _r = requests.post(url, auth=TokenAuth(token), data={'data': _json})

        # for key, value in obj.items():
        #     print(key, value)
    else:
        print('Нет данных для отправки!')
