from collections import defaultdict
from timeit import default_timer
from datetime import datetime

class Logger:

    def __init__(self, func=None):
        self.__logger_dict = defaultdict()
        self.__default_timer()


    def logging_start(self):
        self.__temp_time1 = default_timer()


    def logging_end(self, user_param):
        self.__diff_time = round(default_timer() - self.__temp_time1, 4)
        if user_param in self.__logger_dict.keys():
            self.__logger_dict[user_param] += self.__diff_time
        else:
            self.__logger_dict[user_param] = self.__diff_time
        self.__default_timer()


    def logging_func(self, func):
        def inner(*args, **kwargs):
            self.logging_start()
            res = func(*args, **kwargs)
            self.logging_end(func.__name__)
            return res
        return inner


    def print_results(self):
        print(self.__get_results())


    def __default_timer(self):
        self.__temp_time1 = 0
        self.__diff_time = 0


    def __get_results(self):
        return datetime.now().strftime("%d-%m-%Y, %H:%M") + '\n' +\
        '-' * 15 + 'Время работы' + '-' * 15 + '\n' + \
        '\n'.join([f"{key} - {value} c" for key, value in self.__logger_dict.items()])  + '\n' + \
        '-' * 17 + 'Конец' + '-' * 20


