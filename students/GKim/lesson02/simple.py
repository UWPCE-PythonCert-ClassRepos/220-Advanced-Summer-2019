import logging
import sys

log_format = "%(asctime)s %(filename)s:%(lineno)-3d %(levelname)s %(message)s"

# BEGIN NEW STUFF
formatter = logging.Formatter(log_format)

stream_handler = logging.StreamHandler(sys.stdout)
file_handler = logging.FileHandler('mylog.log')
file_handler.setFormatter(formatter)

logger = logging.getLogger()
logger.addHandler(file_handler)
logger.addHandler(stream_handler)
# END NEW STUFF

def my_fun(n):
    for i in range(0, n):
        logging.debug(i)
        if i == 50:
            logging.warning("The value of i is 50.")
        try:
            i / (50 - i)
        except ZeroDivisionError:
            logging.error("Tried to divide by zero. Var i was {}. Recovered gracefully.".format(i))

if __name__ == "__main__":
    my_fun(100)