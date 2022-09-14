import os
import re
from bs4 import BeautifulSoup
import requests
import json
processed_data = {}


def ps(name):
    head, tail = os.path.split(__file__)
    p1 = os.path.normpath(f'{head}/data/{name}')
    return p1


def route(original_func):
    def wrap_func(value, data=0):
        head, tail = os.path.split(__file__)
        file_folder = os.path.normpath(f'{head}/data/{value}')
        if data == 0:
            rez = original_func(file_folder)
        else:
            rez = original_func(file_folder, data)
        return rez
    return wrap_func


@route
def open_file(file_folder):
    with open(file_folder, 'r', encoding='utf-8') as file:
        data = file.read()
        return data


@route
def write_file(file_folder, data):
    with open(file_folder, 'w', encoding='utf-8') as file:
        file.write(data)


def parser_html(contents):
    soup = BeautifulSoup(contents, 'lxml')
    # _v = soup.select('.generator-table-container')
    # _v = _v.select('tr')
    _v = soup.find_all('div', attrs={'class': 'generator-table-container'})
    _v = _v[0].find_all('tr')
    for item in _v:

        _list = []
        for i in item:
            _list.append(i.text.strip())

        if _list[3] != '':
            if processed_data.get(_list[5]):
                processed_data[_list[5]].append([_list[3], _list[7], _list[9]])
            else:
                processed_data[_list[5]] = []
                processed_data[_list[5]].append([_list[3], _list[7], _list[9]])


def find_file():
    dict_file = {}
    operation = ['purchase', 'sale', 'repurchase']

    for name_file in operation:
        _v = []
        for file_folder in os.listdir(ps(name_file)):
            _v.append(file_folder)
        dict_file[name_file] = _v

    return dict_file


def data_processing(data_array):

    def get_cetegory(_str):
        """Получаем категорию из строки"""
        _rez, cat, sub_cat = '', '', ''

        pattern = r'[(]\d{1,9}\sшт.[)]'
        _str = re.sub(pattern, '', _str).strip()

        _p = _str.split('/')

        cat = _p[0]
        sub_cat = _p[1] if len(_p) > 2 else ''

        _p = _p[2:] if len(_p) > 2 else _p[1:]

        for elem in _p:
            if len(_p) > 1:
                _rez += f'/{elem}'
            else:
                _rez = elem

        return _rez, cat, sub_cat

    def reg_get_things(string="Кабеля/micro-usb/Hoxo X1 Micro-USB (5 шт.)"):
        """Извличение из строки (5 шт.)"""

        pattern = r'[(]\d{1,9}\sшт.[)]'
        _res_name_product = re.sub(pattern, '', string).strip()
        result = re.search(pattern, string)
        _res_storage = re.sub(r'\D', '', result.group(0)) if result else 1
        return _res_storage

    dict_array = {}

    for key, value in data_array.items():
        if key == 'ID':
            continue

        _storage, _sum = 0, 0
        for item in value:
            if item[0] == 'продажа новых товаров':
                _storage -= 1
                _number = int(item[2].replace(' ', ''))
                if _number > _sum:
                    _sum = _number
            elif item[0] == 'докупка новых товаров' or item[0] == 'покупка новых товаров':
                i = reg_get_things(item[1])
                _storage += int(i)
                if _sum == 0:
                    _number = int(item[2].replace(' ', ''))*(-1)
                    _number = int(_number/int(i))
                    _sum = _number

        _name, _cat, _sub_cat = get_cetegory(value[0][1])

        if _storage > 0:
            _m = [_name, _storage, _sum, _cat, _sub_cat]
            dict_array[re.sub('\D', '', key)] = _m

    return dict_array


def sending_data():
    requests.post('https://ch-shop.ru/', data={'key': 'value'})


def save_to_json(data):
    _v = json.dumps(data)
    write_file('json/json.txt', _v)
    # print(_v)


def start():
    data = find_file()
    for item in data:
        for i in data[item]:
            _rez = open_file(f'{item}/{i}')
            parser_html(_rez)
    data = data_processing(processed_data)
    save_to_json(data)


start()
