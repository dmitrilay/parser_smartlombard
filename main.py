import requests
import time
import json
from openpyxl import Workbook
from settings import *

price_list = dict()


def write_html(data, name, format_p='.html'):
    p1 = ps(f'{name}{format_p}')
    with open(p1, 'w', encoding='utf-8') as file:
        file.write(data.text)


def open_convert_html(name):
    """
    Открывает файл в текущей папке и конвертирует из json в словарь
    """
    with open(name, 'r', encoding='utf-8') as file:
        data = file.read()
        data = json.loads(data)
        data1 = data['body']['products']
        data2 = data['body']['total']
        data1 = ','.join(data1)
        data = [data1, data2]
    return data


def get_urls(urls, data, cookies, i):
    response1 = requests.get(urls, params=data, headers=HEADERS, cookies=cookies)
    write_html(response1, i)
    return response1


def post_urls(urls, data, cookies, i):
    pr = data.split(',')
    params = {"productIds": pr, "media": 'true', "categories": 'true', "availability": 'true'}
    response = requests.post(urls, data=params, headers=HEADERS, cookies=cookies)
    write_html(response, i)
    return response


def main():
    i = 0
    res = requests.get(url, headers=HEADERS)
    cookies = dict(res.cookies.items())

    # get_urls(url_personalData, 'personalData')
    product_groups = ['205']
    for pg in product_groups:
        count = 0
        while True:
            params = {'categoryId': pg, 'offset': count, 'limit': '72', 'doTranslit': 'true'}
            get_urls(url_id, params, cookies, f'url_id/url_id{i}')
            pr124 = open_convert_html(ps(f'url_id/url_id{i}.html'))
            product_code = pr124[0]
            post_urls(f'{url_product}', product_code, cookies, f'url_product/url_product{i}')
            params = {'productIds': product_code}
            get_urls(url_prices, params, cookies, f'url_prices/url_prices{i}')
            get_urls(url_statuses, params, cookies, f'url_statuses/url_statuses{i}')
            i += 1
            time.sleep(3)
            print(count)
            count += 72
            counter = pr124[1]
            if count > counter:
                break


def open_convert_html2(name, type_data):
    for file_folder in os.listdir(name):
        if file_folder.endswith(".html"):
            file_folder = os.path.normpath(f'{name}/{file_folder}')
            with open(file_folder, 'r', encoding='utf-8') as file:
                data = file.read()
                data = json.loads(data)
                if type_data == 'product':
                    for i1 in data['body']['products']:
                        price_list[i1['productId']] = [i1['name'], '', '', '']
                elif type_data == 'prices':
                    for i2 in data['body']['materialPrices']:
                        base_price = i2['price']['basePrice']
                        sale_price = i2['price']['salePrice']
                        price_list[i2['productId']][1] = base_price
                        price_list[i2['productId']][2] = sale_price
                elif type_data == 'statuses':
                    for i2 in data['body']['statuses']:
                        product_status = i2['productStatus']
                        price_list[i2['productId']][3] = product_status


def ps(name):
    head, tail = os.path.split(__file__)
    p1 = os.path.normpath(f'{head}/data/{name}')
    # p1 = os.path.normpath(os.getcwd() + '/data/' + name)
    return p1


def file_cleaner():
    file_folder_list = {'url_id': ['url_id', 'url_id/Архив'],
                        'url_prices': ['url_prices', 'url_prices/Архив'],
                        'url_product': ['url_product', 'url_product/Архив'],
                        'url_statuses': ['url_statuses', 'url_statuses/Архив']}

    for i in file_folder_list.values():
        u1 = ps(i[0])
        u2 = ps(i[1])
        for file_folder in os.listdir(u1):
            if file_folder.endswith(".html"):
                head, tail = os.path.split(file_folder)
                file_folder1 = os.path.normpath(f'{u1}/{file_folder}')
                file_folder2 = os.path.normpath(f'{u2}/{tail}')
                os.replace(src=file_folder1, dst=file_folder2)


def writing_file_excel():
    """
    Сохраняем данные в формате excel
    """
    wb = Workbook()
    ws = wb.active

    i = 0
    for pr in price_list.values():
        if pr[3] == 'Available':
            ws.cell(row=i + 1, column=1, value=pr[0])
            ws.cell(row=i + 1, column=2, value=pr[1])
            ws.cell(row=i + 1, column=3, value=pr[2])
            ws.cell(row=i + 1, column=4, value=pr[3])
            i += 1

    p0 = "C:/Users/dmitr/OneDrive/Документы/1_Parser/mvideo1.xlsx"
    p1 = os.path.normpath(p0)
    wb.save(filename=p1)
