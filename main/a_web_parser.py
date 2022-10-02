from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
import os
from time import sleep
import pickle
from settings import *

from datetime import date
from a_file_system import WorkFolderFiles


class WebParser():
    def __init__(self) -> None:
        self.wb = None
        self.web()

    def web(self):
        address, name_file = os.path.split(__file__)
        options = Options()
        options.add_experimental_option('prefs', options_web)
        options.binary_location = "C:\\\Programs\\Chrome\\\Application\\chrome.exe"
        name_ch = os.path.normpath(f'{address}/chromedriver/chromedriver.exe')
        self.wb = webdriver.Chrome(name_ch, options=options)

    def authorization(self):
        reauthorization = False
        self.wb.get(url)

        check_file = os.path.exists('cookies.pkl')
        if check_file:
            cookies = pickle.load(open("cookies.pkl", "rb"))
            self.wb.delete_all_cookies()

            for cookie in cookies:
                self.wb.add_cookie(cookie)

            sleep(3)
            self.wb.get(url)
            sleep(2)

            account_info = self.wb.find_elements(By.CLASS_NAME, "account-info")
            if len(account_info) == 0:
                reauthorization = True
        else:
            reauthorization = True

        if reauthorization:
            self.wb.delete_all_cookies()
            sleep(2)
            self.wb.find_element(By.ID, "log").send_keys(username)
            self.wb.find_element(By.ID, "nam").send_keys(password)
            sleep(1)
            self.wb.find_element(By.ID, 'sub').click()
            sleep(2)
            pickle.dump(self.wb.get_cookies(), open("cookies.pkl", "wb"))

    def action(self, operation, date_start='02.07.2022', date_end='01.08.2022'):
        wb = self.wb
        # выбор типа операции в select
        select_limit = wb.find_element(By.CSS_SELECTOR, "select[name='_limit']")
        select_object = Select(select_limit)
        select_object.select_by_value('500')
        sleep(5)

        filter_date_start = wb.find_element(By.ID, "filter-date-start")
        filter_date_end = wb.find_element(By.ID, "filter-date-end")
        btn = wb.find_element(By.CLASS_NAME, "table-generator-submit-button")
        # select_element = wb.find_element(By.ID,'selectElementID')
        select_operation = wb.find_element(By.CSS_SELECTOR, "select[name='type_operation']")

        filter_date_start.clear()
        filter_date_end.clear()
        filter_date_start.send_keys(date_start)
        filter_date_end.send_keys(date_end)

        # выбор типа операции в select
        select_object = Select(select_operation)
        select_object.select_by_value(operation)

        sleep(2)
        btn.click()
        sleep(4)

    # def save_html(self, operations, date):
    #     pageSource = self.wb.page_source
    #     folder_name = f'{operations}/{operations}_{date[0]}-{date[1]}.html'
    #     return [folder_name, pageSource]


def start_web_parser(date_p=None, date_list=None):
    """
    30 purchase - покупка новых товаров
    31 sale - продажа новых товаров
    32 repurchase - докупка новых товаров
    """
    ff = WorkFolderFiles()
    obj = WebParser()
    obj.authorization()

    _d = date.today().strftime('%d.%m.%Y') if date_p == None else date_p
    date_list = [[_d, _d], ] if date_list == None else date_list

    operation_dict = {'purchase': '30', 'sale': '31', 'repurchase': '32'}

    for dt in date_list:
        start, end = dt[0], dt[1]
        day_or_month = 'day' if int(start[0:2]) == int(end[0:2]) else 'month'

        for operations in operation_dict:
            obj.action(operation=operation_dict[operations], date_start=start, date_end=end)
            folder_name = f'{day_or_month}/{operations}/{operations}_{start}-{end}.html'
            ff.write_file(folder_name, obj.wb.page_source)
