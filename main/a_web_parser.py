from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
import os
from time import sleep
import pickle
from settings import *
from c_file_system import *


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

    def save_html(self, operations, date):
        pageSource = self.wb.page_source
        folder_name = f'{operations}/{operations}_{date[0]}-{date[1]}.html'
        return [folder_name, pageSource]


def start():
    """
    30 purchase - покупка новых товаров
    31 sale - продажа новых товаров
    32 repurchase - докупка новых товаров
    """
    obj = WebParser()
    obj.authorization()

    data_set_list = [['02.07.2022', '01.08.2022'],
                     ['02.06.2022', '01.07.2022'],
                     ['02.05.2022', '01.06.2022'],
                     ['02.04.2022', '01.05.2022'],
                     ['02.03.2022', '01.04.2022']]

    # obj.action(operation='31', date_start='02.07.2022', date_end='01.08.2022')

    # operation_dict = {'purchase': '30', 'sale': '31', 'repurchase': '32'}
    operation_dict = {'sale': '31'}

    for date in data_set_list:
        for operations in operation_dict:
            obj.action(operation=operation_dict[operations], date_start=date[0], date_end=date[1])
            folder_name, pageSource = obj.save_html(operations, date)
            WorkFolderFiles.write_file(folder_name, pageSource)


start()
