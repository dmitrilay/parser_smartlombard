import os
import json
import csv

head, tail = os.path.split(__file__)
BASE_DIR = os.path.join(head, 'data')


class WorkFolderFiles():
    def __init__(self, search_folder='html_page'):
        """search_folder - будем искать файлы в этой папке"""
        self.search_folder = search_folder
        self.list_file = {}
        self.data = None
        self.json_data = None

    def find_file(self, search_folder):
        _path = os.path.join(BASE_DIR, search_folder)
        for file_folder in os.listdir(_path):
            full_path = os.path.join(_path, file_folder)
            self.list_file[file_folder] = [full_path, file_folder]

    def open_file(self, file_folder):
        _isfile = False
        _path = os.path.join(BASE_DIR, file_folder)
        _path = os.path.normpath(_path)

        if os.path.isfile(file_folder):
            _isfile = True
        elif os.path.isfile(_path):
            _isfile = True
            file_folder = _path

        self.data = ''
        if _isfile:
            with open(file_folder, 'r', encoding='utf-8') as file:
                self.data = file.read()

    def save_to_json(self, obj=None, name_file=None):
        _path = os.path.normpath(f'{BASE_DIR}/{name_file}')
        self.json_data = json.dumps(obj)
        self.write_file(_path, self.json_data)

    def open_to_json(self, name_file=None):
        _path = os.path.normpath(f'{BASE_DIR}/{name_file}')
        self.open_file(_path)
        if self.data:
            self.json_data = json.loads(self.data)
            return self.json_data
        else:
            return None

    @staticmethod
    def write_file(name_file, obj):
        _path = os.path.join(BASE_DIR, name_file)
        with open(_path, 'w', encoding='utf-8') as file:
            file.write(obj)

    @staticmethod
    def open_file_csv(file_folder):
        head, tail = os.path.split(__file__)
        file_folder = os.path.normpath(f'{head}/data/{file_folder}')
        with open(file_folder, 'r', encoding='utf-8') as file:
            file_reader = csv.reader(file, delimiter=",")
            return (list(file_reader))


# file = WorkFolderFiles()
# file.find_file()
# print(file.list_file)
