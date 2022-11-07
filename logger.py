from collections import defaultdict
from timeit import default_timer


class Logger:

    def __init__(self):
        self.__logger_dict = defaultdict()
        self.__default_timer()

    def logging_start(self):
        self.__temp_time1 = default_timer()

    def logging_end(self, user_param):
        self.__temp_time2 = default_timer()
        if user_param in self.__logger_dict.keys():
            self.__logger_dict[user_param] += self.__temp_time2 - self.__temp_time1
        else:
            self.__logger_dict[user_param] = self.__temp_time2 - self.__temp_time1
        self.__default_timer()

    def __default_timer(self):
        self.__temp_time1 = 0
        self.__temp_time2 = 0

    def print_results(self):
        print('Время работы:')
        [print(f'"{key}" - {value} c') for key, value in self.__logger_dict.items()]
        print('-------Конец-------')
