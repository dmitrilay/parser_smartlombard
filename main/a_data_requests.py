import json
import requests
from requests.auth import AuthBase


class TokenAuth(AuthBase):
    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        r.headers['X-TokenAuth'] = f'{self.token}'
        return r


token = "fjwoapfjow@204diojwa!24dkapwojfjjf22401jdwa190jd(odwa"


def sending_spec(obj=0):
    if obj:
        pathname = 'smartlombard/v2/'
        host = 'http://127.0.0.1:8000/'
        url = f'{host}{pathname}'

        _json = json.dumps(obj)
        # url = 'http://127.0.0.1:8000/spec/add-characteristic-ajax/'
        _r = requests.post(url, auth=TokenAuth(token), data={'data': _json})

        # print(obj)
        for key, value in obj.items():
            print(key, value)
    else:
        print('Нет данных для отправки!')
