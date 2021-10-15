import os

url = 'https://www.mvideo.ru/smartfony-i-svyaz-10/smartfony-205'
# url.append('https://www.mvideo.ru/televizory-i-cifrovoe-tv-1/televizory-65')

url_personalData = 'https://www.mvideo.ru/bff/personalData'
url_settings = 'https://www.mvideo.ru/bff/settings'

url_id = f'https://www.mvideo.ru/bff/products/listing'

url_product = 'https://www.mvideo.ru/bff/product-details/'
url_prices = 'https://www.mvideo.ru/bff/products/prices'  # нужно подставить коды товаров
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
