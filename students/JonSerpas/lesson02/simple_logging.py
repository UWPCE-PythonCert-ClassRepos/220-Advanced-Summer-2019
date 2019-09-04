import logging
import sys

log_format = "%(asctime)s\t%(filename)s\t%(lineno)d\t%(levelname)s\t%(message)s"

# logging.basicConfig(level=logging.WARNING, format=log_format, filename='simple.log')

formatter = logging.Formatter(log_format)

stream_handler = logging.StreamHandler(sys.stdout)
file_handler = logging.FileHandler("simple.log")

file_handler.setFormatter(formatter)
# stream_handler = setFormatter(formatter)

logger = logging.getLogger()
logger.addHandler(file_handler)
logger.addHandler(stream_handler)


def fun(n):
    for i in range(0, n):
        if i == 50:
            logging.warning('oh snap, i == 50')
        try:
            100 / (50 - i)
        except ZeroDivisionError:
            logging.debug('zero division error')

if __name__ == "__main__":
    fun(100)