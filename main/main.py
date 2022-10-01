from a_web_parser import start_web_parser
from a_html_processing import start_changes_day, start_changes_month, save_to_last_session
from a_data_requests import sending_spec


# auto
start_web_parser()
current_data, previous_data = start_changes_day()
sending_spec(current_data)
save_to_last_session(previous_data)


# Test
"""Проверка по месяцу шаг в один день"""
# _m = [f'{str(x).rjust(2,"0")}.09.2022' for x in range(2, 31)]

# for _d in _m:
#     # start_web_parser(_d)
#     data = start_changes_day( _d)
#     sending_spec(data)
#     # save_to_last_session(data, _d)
#     print('===================', _d)

"""Проверка по дню"""
# _d = '01.10.2022'
# start_web_parser(_d)
# current_data, previous_data = start_changes_day(_d)
# sending_spec(current_data)
# save_to_last_session(previous_data, _d)


"""Массовая загрузка данных"""
# m_date = [['02.08.2022', '01.09.2022'],
#           ['02.07.2022', '01.08.2022'],
#           ['02.06.2022', '01.07.2022'],
#           ['02.05.2022', '01.06.2022'],
#           ['02.04.2022', '01.05.2022'],
#           ['02.03.2022', '01.04.2022'],
#           ]

# # start_web_parser(date_list=m_date)
# data = start_changes_month(m_date)
# sending_spec(data)
