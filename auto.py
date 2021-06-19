


def write_html(html):
    with open('test.html', 'w', encoding='utf-8') as file:
        file.write(html.text + '\n')
    print(html.text)


# def get_content(html):
#     soup = BeautifulSoup(html, 'html.parser')
#     items = soup.find_all('a', class_='proposition_link')
#     print(items)

# if RECORDING_COOKIES:
#     write_txt(session.cookies)


# def write_txt(name):
#     with open(ps(name), 'w', encoding='utf-8') as file:
#         file.write(str(name))



def writing_file_excel_db(self, path_to_save='database_excel.xlsx'):
    """
    Сохраняем базу данных в формате excel
    """
    wb = Workbook()
    ws = wb.active
    stop_for = len(self.price_db['Наименование'])
    for i in range(0, stop_for):
        ws.cell(row=i + 1, column=1, value=self.price_db['Наименование'][i])
        ws.cell(row=i + 1, column=2, value=self.price_db['Цена'][i])
        ws.cell(row=i + 1, column=3, value=self.price_db['Цена2'][i])
        ws.cell(row=i + 1, column=4, value=self.price_db['дата'][i])
        ws.cell(row=i + 1, column=5, value=self.price_db['Вывод'][i])

    wb.save(filename=path_to_save)

from ParsFile import *


my_list_file = ['dns.xlsx', 'mts.xlsx', 'mvideo1.xlsx', 'mvideo2.xlsx', 'eldorado.xlsx']
archive_file = os.path.join(PathOpen, 'Архив')
current_time = datetime.datetime.now().strftime("%d-%m-%y_%H-%M") + '_'

input_data = {'mvideo1.xlsx': [db1, 'mvideo'],
              'mvideo2.xlsx': [db1, 'mvideo'],
              'dns.xlsx': [db3, 'dns'],
              'mts.xlsx': [db2, 'mts'],
              'eldorado.xlsx': [db4, 'eldorado'], }

for file_folder in os.listdir(PathOpen):
    for my_files in my_list_file:
        if file_folder == my_files:
            u1 = os.path.join(PathOpen, file_folder)
            u2 = os.path.join(archive_file, current_time + file_folder)
            pr1 = input_data.get(my_files)
            if pr1 is not None:
                pm = ParserFile(path_to_open=u1, path_to_save=PathSave, db=pr1[0], mg=my_files)
                pm.open_file()
                pm.unloading_from_the_database()
                pm.find_in_the_database()
                # os.replace(src=u1, dst=u2)
