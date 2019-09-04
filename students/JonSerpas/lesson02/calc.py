import logging
import json

log_format = "%(asctime)s\t%(message)s"
formatter = logging.Formatter(log_format)
file_handler = logging.FileHandler("calc.log")
file_handler.setFormatter(formatter)
logger = logging.getLogger()
logger.addHandler(file_handler)

if __name__ == "__main__":
    print('Welcome to CALC')
    print('Please math happen')
    while True:
        try:
            expression = input('= ')
            if expression in ('exit', 'quit'):
                exit(0)
            result = eval(expression)
            if result:
                print(result)
        except Exception as exception:
            logging.error(
                json.dumps({
                    "name": type(exception).__name__,
                    "msg": str(exception)
                    })
                )
