import os

url_start = 'https://www.mvideo.ru'
url_id = f'https://www.mvideo.ru/bff/products/listing'
url_product = 'https://www.mvideo.ru/bff/product-details/'
url_prices = 'https://www.mvideo.ru/bff/products/prices'
url_statuses = 'https://www.mvideo.ru/bff/products/statuses'

HEADERS = {
    'Host': 'www.mvideo.ru',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0',
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.mvideo.ru/smartfony-i-svyaz-10/smartfony-205/f/category=smartfony-761',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'TE': 'trailers',
}
DEBUG = True
if DEBUG:
    product_groups = ['205']
    path_file_save = os.path.normpath("C:/Users/dmitr/OneDrive/Документы/1_Parser/mvideo1.xlsx")
else:
    product_groups = ['118', '65', '205', '159', '89']
    path_file_save = os.path.normpath("D:/Parse/parser_data/mvideo.xlsx")
