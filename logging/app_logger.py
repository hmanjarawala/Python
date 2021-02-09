# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 12:53:53 2020

@author: Himanshu.Manjarawala
"""

import logging
import logging.config
import yaml
import sys
import os
import datetime
from threading import Lock

class LogManagerMeta(type):
    """
    This is a thread-safe implementation of Singleton.
    """

    _instances = {}

    _lock: Lock = Lock()
    """
    We now have a lock object that will be used to synchronize threads during
    first access to the Singleton.
    """

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        # Now, imagine that the program has just been launched. Since there's no
        # Singleton instance yet, multiple threads can simultaneously pass the
        # previous conditional and reach this point almost at the same time. The
        # first of them will acquire lock and will proceed further, while the
        # rest will wait here.
        with cls._lock:
            # The first thread to acquire the lock, reaches this conditional,
            # goes inside and creates the Singleton instance. Once it leaves the
            # lock block, a thread that might have been waiting for the lock
            # release may then enter this section. But since the Singleton field
            # is already initialized, the thread won't create a new object.
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class LogManager(metaclass=LogManagerMeta):
    __logFilePath: str = None
    
    def __init__(self, logFilePath) -> None:
        self.__logFilePath = logFilePath
        if not os.path.exists(self.__logFilePath):
            os.makedirs(self.__logFilePath)
        
        now = datetime.datetime.now().strftime("%Y_%m_%d")
        dynamic_log_name = f'{self.__logFilePath}\HistoryLog_{now}.log'
        configString = "version: 1\n"\
                           "formatters:\n"\
                           "  simple:\n"\
                           "    format: '%(asctime)s - %(levelname)s - %(message)s'\n"\
                           "  colored:\n"\
                           "    format: '%(log_color)s%(asctime)s%(reset)s - %(log_color)s%(levelname)s%(reset)s - %(log_color)s%(message)s%(reset)s'\n"\
                           "    class: colorlog.ColoredFormatter\n"\
                           "handlers:\n"\
                           "  console:\n"\
                           "    class: logging.StreamHandler\n"\
                           "    level: DEBUG\n"\
                           "    formatter: colored\n"\
                           "    stream: ext://sys.stdout\n"\
                           "  file:\n"\
                           "    class : logging.handlers.RotatingFileHandler\n"\
                           "    formatter: simple\n"\
                           f"    filename: {dynamic_log_name}\n"\
                           "    maxBytes: 10485760\n"\
                           "    backupCount: 3\n"\
                           "loggers:\n"\
                           "  sampleLogger:\n"\
                           "    level: DEBUG\n"\
                           "    handlers: [console]\n"\
                           "    propagate: no\n"\
                           "  fileLogger:\n"\
                           "    level: DEBUG\n"\
                           "    handlers: [file]\n"\
                           "root:\n"\
                           "  level: DEBUG\n"\
                           "  handlers: [console]"
        # log_level = logging.DEBUG
        # log_format = '%(log_color)s%(asctime)s%(reset)s - %(log_color)s%(levelname)s%(reset)s - %(log_color)s%(message)s%(reset)s'
        # formatter = ColoredFormatter(log_format)
        # logging.root.setLevel(log_level)
        # stream = logging.StreamHandler()
        # stream.setLevel(log_level)
        # stream.setFormatter(formatter)
        # logging.root.addHandler(stream)
        # file = logging.handlers.RotatingFileHandler(filename=dynamic_log_name,maxBytes=10485760,backupCount=3)
        # file.setFormatter(logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(message)s'))
        # file.setLevel(log_level)
        config = yaml.safe_load(configString)
        logging.config.dictConfig(config)
        self.__logger = logging.getLogger('fileLogger')
        # self.__logger.setLevel(log_level)
        # self.__logger.addHandler(file)
        
    def get_logger(self) -> None:
        return self.__logger


def getLogger():
    logMgr = LogManager(os.path.join(getApplicationPath(), 'Logs'))
    return logMgr.get_logger()

def getmsg(name, msg):
    return f'{name} - {msg}'

def getApplicationPath():
    if getattr(sys, 'frozen', False):
        application_path = os.path.dirname(sys.executable)
    elif __file__:
        application_path = os.path.dirname(__file__)

    return application_path

if __name__ == '__main__':
    logger = getLogger()
    logger.info('Info!!')
    logger.debug("Debug!!")
    logger.warning("Warning!!")
    logger.error("Error!!")
    logger.critical("Critical!!")
    try:
        k = 5/0
    except Exception as e:
        exc_info = sys.exc_info()
        logger.exception(exc_info)