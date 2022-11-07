from collections import defaultdict
from timeit import default_timer


class Logger:

    def __init__(self):
        self.__logger_dict = defaultdict()
        self.__temp_time = 0

    def logging_start(self):
        self.__temp_time = default_timer()

    def logging_end(self, user_param):
        self.__logger_dict[user_param] = self.__temp_time - default_timer()