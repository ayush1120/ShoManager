import os,logging


logger = logging.getLogger("Logger")


logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('Date & Time      : %(asctime)s\n'
                              'Logger Name      : %(name)s\n'
                              'Level Name       : %(levelname)s\n'
                              'Calling Function : %(funcName)s\n'
                              'Message          : %(message)s\n')

file_handler = logging.FileHandler('Log.log',mode='a')

file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

def func_Kill():
    logger.debug('I\'m Killin It')

func_Kill()
