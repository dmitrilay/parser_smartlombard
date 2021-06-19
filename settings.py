import os

url = 'https://www.mvideo.ru/smartfony-i-svyaz-10/smartfony-205'
# url.append('https://www.mvideo.ru/televizory-i-cifrovoe-tv-1/televizory-65')

url_personalData = 'https://www.mvideo.ru/bff/personalData'
url_settings = 'https://www.mvideo.ru/bff/settings'

url_id = f'https://www.mvideo.ru/bff/products/listing?categoryId='
url_product = 'https://www.mvideo.ru/bff/products?productIds='  # нужно подставить коды товаров
url_prices = 'https://www.mvideo.ru/bff/products/prices?productIds='  # нужно подставить коды товаров
url_statuses = 'https://www.mvideo.ru/bff/products/statuses?productIds='

HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36',
    'accept': '*/*'
}
HEADERS2 = {
    'Host': 'www.mvideo.ru',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Accept': 'application/json',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.mvideo.ru/smartfony-i-svyaz-10/smartfony-205',
    'Connection': 'keep-alive',
    # 'Cookie': 'MVID_CITY_ID=CityCZ_9909; MVID_GUEST_ID=17542191110; JSESSIONID=cX2vgHrX2zwDm1Mpf1rKgTK5qNSJNtppKnyQT74GQL2Qs0C2NQn1!362256321; MVID_REGION_ID=30; COMPARISON_INDICATOR=false; CACHE_INDICATOR=false; flacktory=no; bIPs=-957002303; MVID_TIMEZONE_OFFSET=6; MVID_KLADR_ID=5500000100000; MVID_REGION_SHOP=S935; MVID_GEOLOCATION_NEEDED=true; BIGipServericerock-prod=3187989514.20480.0000; _gaexp=GAX1.2.apYSYezxSAq2h3MRe5qu8Q.18875.0!PMzTxNvETtW8s2x75uEILg.18881.1!-n-23KtbS5OAglnwhXL-oQ.18869.1; _ga=GA1.2.16703147.1623694046; _gid=GA1.2.1452067782.1623694046; _gcl_au=1.1.1910109020.1623694046; _ga_CFMZTSS5FM=GS1.1.1623694045.1.1.1623697302.0; _ga_BNX5WPP3YK=GS1.1.1623694045.1.1.1623697302.57; _ym_uid=1623677007899417554; _ym_d=1623694047; tmr_reqNum=150; tmr_lvid=69bec5c54d61bdc2d0facb0838687bc1; tmr_lvidTS=1623677005967; _fbp=fb.1.1623694047911.1443771183; _ym_isad=2; cfidsgib-w-mvideo=u9VYzFWjgtAZo3ZMBete/MRUXCpwrMO1Aj5wmK6hQZxA/KBqETSBm7Cbs8A/8QDnrh7MtZGvz2mn5ueszkwz7gCsfZyGB0OXmhEtzlbVlSSpaF33e38welP/3dUsi+2rlCHwSOH1BbpB7uNFrZQXq/KoVdkqEMRvQuvQ8ngn; afUserId=1221b87a-d886-4174-97c7-fdb41503b17f-p; cto_bundle=ilFrh19sNFZTUDI4TVVlUXExUmRqWGJheXpTSE5IU09XWEdRVEFiYThuVUFOeVR5ejAlMkJzN3BEZzhKWjdPd3AyRlplR0MweExWT0dKZTk5YnFVblNTVThpbTNGcEo4JTJCbGtEbHBoN3VGcGF6aU53UWpiUms0MjJkWkI3R0lRRnZOQTc2aWU0ZWtXNjNJV2tWQ2h6cXVtNERJRU1RJTNEJTNE; __zzatgib-w-mvideo=MDA0dBA=Fz2+aQ==; AF_SYNC=1623694052234; gsscgib-w-mvideo=jiylhq8pFpg/U30SURZoAqYggPk941hO3cOCbXbA42tK4NYv9yF40kkjpTXrt6AnyDndzvFn6HXTmKYi4qhxcUBSoNCFSNM9fjkHb2O1k6PPFWIUDMQAAcSNhnkkjluKxPvTCM/ImHc3oE76FKD7IM3xTphb3w/PPuyH/C7t9bok3hxqTm+XOSEsWYA+C+Va2R50qgW57/FHSdMTENo/Lb5wibR7UhCxEuneD4R3M8F1ijRYtN/uOyR2bpMo9g==; tmr_detect=0%7C1623697307282; ADRUM=s=1623698326711&r=https%3A%2F%2Fwww.mvideo.ru%2Fsmartfony-i-svyaz-10%2Fsmartfony-205%3F0; MVID_GET_LOCATION_BY_DADATA=DaData; NEED_REQUIRE_APPLY_DISCOUNT=true; HINTS_FIO_COOKIE_NAME=2; PROMOLISTING_WITHOUT_STOCK_AB_TEST=2; searchType2=2; MVID_YA_BLOCKER=1; BIGipServeratg-ps-prod_tcp80=1225055242.20480.0000; BIGipServeratg-ps-prod_tcp80_clone=1225055242.20480.0000; swp_token=1623699721:45d1e81458f1a33c2e846afa87e39dc1:8d5bdd2e2d72d87fbd14a25f1f22a30d; wurfl_device_id=generic_web_browser; deviceType=desktop; SMSError=; authError=; GO_apYSYezxSAq2h3MRe5qu8Q=0; GO_PMzTxNvETtW8s2x75uEILg=1',
    'Pragma': 'no-cache',
    'Cache-Control': 'max-age=0, no-cache',
    'TE': 'Trailers',
}
