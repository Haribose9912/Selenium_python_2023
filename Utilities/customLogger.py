import logging
import inspect


def configure_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Define the log file path
    log_file = 'Logs/log_file.log'

    # Create a file handler and set its level to INFO
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.INFO)

    # Create a formatter and add it to the file handler
    formatter = logging.Formatter('%(asctime)s :%(levelname)s : %(name)s :%(message)s')
    file_handler.setFormatter(formatter)

    # Add the file handler to the logger
    logger.addHandler(file_handler)

    return logger

# # class LogGen:
# @staticmethod
# def loggen():
#     logging.basicConfig(filename="demo.log",
#                         format='%(asctime)s - %(levelname)s - %(message)s',
#                         datefmt='%Y/%m/%d %H:%M:S %p')
#     return logging.getLogger()
