import logging
import inspect


# class LogGen:
#     @staticmethod
def loggen():
    logging.basicConfig(filename="demo.log",
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        datefmt='%Y/%m/%d %H:%M:S %p')
    return logging.getLogger()
