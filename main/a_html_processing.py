from datetime import datetime
import re
from bs4 import BeautifulSoup
from a_file_system import *
from datetime import date


class HtmlProcessing():
    def __init__(self):
        self.processed_data = {}
        self.contents = None
        self.result = None

    def data_comparison(self, prev):
        curr = self.result
        new_arrow = {}

        for key, value in curr.items():
            if prev.get(key):
                j_storage = prev[key][1]
                p_storage = value[1]
                if p_storage != j_storage:
                    difference = p_storage - j_storage
                    new_arrow[key] = value.copy()
                    new_arrow[key][1] = difference
            else:
                new_arrow[key] = value.copy()

        return new_arrow

    def parser_html(self, page_html):
        data = self.processed_data
        soup = BeautifulSoup(page_html, 'lxml')

        _v = soup.find_all('div', attrs={'class': 'generator-table-container'})
        _v = _v[0].find_all('tr')

        try:
            for item in _v:
                _list = []
                for i in item:
                    _list.append(i.text.strip())

                if _list[3] != '':
                    if data.get(_list[5]):
                        data[_list[5]].append([_list[3], _list[7], _list[9]])
                    else:
                        data[_list[5]] = []
                        data[_list[5]].append([_list[3], _list[7], _list[9]])
        except:
            pass

    def data_processing(self):
        data_array = self.processed_data
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
                    i = self.reg_get_things(item[1])
                    _storage += int(i)
                    if _sum == 0:
                        _number = int(item[2].replace(' ', ''))*(-1)
                        _number = int(_number/int(i))
                        _sum = _number

            _name, _cat, _sub_cat = self.get_cetegory(value[0][1])

            if _storage > 0:
                _m = [_name, _storage, _sum, _cat, _sub_cat]
                dict_array[re.sub('\D', '', key)] = _m

        self.result = dict_array

    def data_processing_one_day(self):
        data_array = self.processed_data
        dict_array = {}

        for key, value in data_array.items():
            if key == 'ID':
                continue

            _storage, price_per_unit = 0, 0
            for item in value:
                _ = [item[0], item[1], abs(int(item[2].replace(' ', ''))), self.reg_get_things(item[1])]
                q_type_operation, q_name, q_price, q_storage = _

                if q_type_operation == 'продажа новых товаров':
                    _storage -= q_storage if q_storage > 0 else 1
                    if q_price > price_per_unit:
                        price_per_unit = q_price

                elif q_type_operation == 'докупка новых товаров' or q_type_operation == 'покупка новых товаров':
                    _storage += q_storage
                    if price_per_unit == 0:
                        price_per_unit = int(q_price/q_storage)

            _name, _cat, _sub_cat = self.get_cetegory(value[0][1])

            if _storage != 0:
                _m = [_name, _storage, price_per_unit, _cat, _sub_cat]
                dict_array[re.sub('\D', '', key)] = _m

        self.result = dict_array

    @staticmethod
    def reg_get_things(string="Кабеля/micro-usb/Hoxo X1 Micro-USB (5 шт.)"):
        """Извличение из строки (5 шт.)"""
        pattern = r'[(]\d{1,9}\sшт.[)]'
        # _res_name_product = re.sub(pattern, '', string).strip()
        result = re.search(pattern, string)
        _res_storage = int(re.sub(r'\D', '', result.group(0)) if result else 1)
        return _res_storage

    @staticmethod
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


def start_changes_month(p_date):
    """Управляющая функция - Парсинг списка html файлов"""
    obj = WorkFolderFiles()
    handler = HtmlProcessing()

    list_file_name = []
    for dt in p_date:
        start, end = dt[0], dt[1]
        list_file_name.append(f'month/purchase/purchase_{start}-{end}.html')
        list_file_name.append(f'month/repurchase/repurchase_{start}-{end}.html')
        list_file_name.append(f'month/sale/sale_{start}-{end}.html')

    for item in list_file_name:
        obj.open_file(item)
        handler.parser_html(obj.data)

    handler.data_processing()
    return handler.result


def start_changes_day(date_p=0):
    _d = date.today().strftime('%d.%m.%Y') if date_p == 0 else date_p

    obj = WorkFolderFiles()
    handler = HtmlProcessing()

    urls = [f'day/purchase/purchase_{_d}-{_d}.html',
            f'day/repurchase/repurchase_{_d}-{_d}.html',
            f'day/sale/sale_{_d}-{_d}.html']

    for item in urls:
        obj.open_file(item)
        handler.parser_html(obj.data)
    handler.data_processing_one_day()
    last_session = obj.open_to_json(name_file=f'json/last_session_{_d}.txt')
    if last_session:
        result = handler.data_comparison(last_session)
        return [result, handler.result]
    else:
        return [handler.result, handler.result]


def save_to_last_session(data, date_p=None):
    """Выполняем в случае успешной отправки на сервер"""
    _d = date.today().strftime('%d.%m.%Y') if date_p == None else date_p
    if data:
        WorkFolderFiles().save_to_json(obj=data, name_file=f'json/last_session_{_d}.txt')
