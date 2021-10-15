from main import *

while True:
    p1 = input('Выбери действие:\n'
               '1. Запустить парсер\n'
               '2. Распарсить данные\n'
               '3. Запись в excel\n'
               '4. Выход\n')
    if p1 == '1':
        print('Сканируем сайт...\n')
        main()
    elif p1 == '2':
        open_convert_html2(ps('url_product'), 'product')
        open_convert_html2(ps('url_prices'), 'prices')
        open_convert_html2(ps('url_statuses'), 'statuses')
        print('Операция выполнена!\n')
    elif p1 == '3':
        writing_file_excel()
        # file_cleaner()
    elif p1 == '4':
        print('Выходим...\n')
        break
    else:
        print('недопустимое значение\n')
