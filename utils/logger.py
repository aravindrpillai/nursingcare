import logging
from datetime import datetime
from nursingcare.settings import BASE_DIR

fileName = "C:/tmp/logs/log_" + (datetime.now().strftime("%Y_%m_%d")) + ".log"

''''
    Class : Loggers
    Desc  : Logs the data
    date  : 29 November 2021
'''


class Logger():
    logging.basicConfig(filename=fileName,
                        filemode='a',
                        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                        datefmt='%H:%M:%S',
                        level=logging.DEBUG)

    @staticmethod
    def info(message):
        logging.info(message)

    @staticmethod
    def debug(message):
        logging.debug(message)

    @staticmethod
    def fatal(message):
        logging.fatal(message)

    @staticmethod
    def error(message):
        logging.error(message)

    @staticmethod
    def critical(message):
        logging.critical(message)
