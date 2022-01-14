from main import *

print('Начнем...')
main()
time.sleep(1.0)
open_convert_html2(ps('url_product'), 'product')
open_convert_html2(ps('url_id'), 'id')
open_convert_html2(ps('url_prices'), 'prices')
open_convert_html2(ps('url_statuses'), 'statuses')
writing_file_excel()
time.sleep(1.0)
file_cleaner()
