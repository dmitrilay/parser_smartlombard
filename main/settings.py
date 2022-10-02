import os
import datetime

"""Авторизация"""
url = 'https://online.smartlombard.ru/login/'
username = "admin@ch-shop.ru"
password = "58800111"

"""Настройки браузера"""
options_web = {
    # 'profile.managed_default_content_settings.javascript': 2,
    # 'profile.managed_default_content_settings.images': 2,
    # 'profile.managed_default_content_settings.mixed_script': 2,
    # 'profile.managed_default_content_settings.media_stream': 2,
    # 'profile.managed_default_content_settings.stylesheets': 2
}


"""Файловая система"""
FOLDERS = [
    'json',
    'day/purchase',
    'day/repurchase',
    'day/sale',
    'month/purchase',
    'month/repurchase',
    'month/sale',
]
