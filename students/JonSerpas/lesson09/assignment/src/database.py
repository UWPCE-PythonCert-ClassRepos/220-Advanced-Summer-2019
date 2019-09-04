import argparse
import logging
import sys
from pymongo import MongoClient


class MongoDBConnection(object):
    """MongoDB Connection"""

    def __init__(self, host='localhost', port='27017'):
        self.host = f"mongodb://{host}:{port}"
        self.connection = None

    def __enter__(self):
        self.connection = MongoClient(self.host)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()


# docker container run --name mongo -p 27017:27017 -d mongo mongod

with MongoDBConnection() as mongo:
    conn = mongo.connection
    db = conn.my_app
    collection = db.people

    # clear the deck
    collection.delete_many({})

    # insert data
    collection.insert_many([
        {
            "first_name": "Lisetta",
            "last_name": "Bennitt",
            "email": "lbennitt0@typepad.com"
        }, {
            "first_name": "Maurits",
            "last_name": "Trazzi",
            "email": "mtrazzi1@mysql.com"
        }, {
            "first_name": "Mandel",
            "last_name": "Handover",
            "email": "mhandover2@weebly.com"
        }
    ])

    # find person
    person = collection.find({"first_name": "Mandel"})
pprint(list(person))


logger = logging.getLogger('app')
logify_level = logging.ERROR

help_statement = """
Accepts integers of corresponding logging levels    
CRITICAL: 50
ERROR: 40
WARNING: 30
INFO: 20
DEBUG: 10
"""

parser = argparse.ArgumentParser()
parser.add_argument(
    '--level_some',
    type=int,
    default=logging.ERROR,
    help=help_statement)
args = parser.parse_args()


class logify:
    def __init__(self, logger, level=None, handler=None, close=True):
        self.logger = logger
        self.level = level
        self.handler = handler
        self.close = close

    def __enter__(self):
        if self.level is not None:
            self.old_level = self.logger.level
            self.logger.setLevel(self.level)
        if self.handler:
            self.logger.addHandler(self.handler)

    def __exit__(self, et, ev, tb):
        if self.level is not None:
            self.logger.setLevel(self.old_level)
        if self.handler:
            self.logger.removeHandler(self.handler)
        if self.handler and self.close:
            self.handler.close()
        # implicit return of None => don't swallow exceptions

    def __call__(self, func):
        def wrapper(*args, **kwds):
            with self:
                return func(*args, **kwds)
        return wrapper


@logify(logger, level=args.level_some)
def some_func():
    logger.debug("some func DEBUG")
    logger.info("some func INFO")
    logger.warning("some func WARNING")
    logger.error("some func ERROR")
    logger.critical("some func CRITICAL")


if __name__ == '__main__':
    logger.addHandler(logging.StreamHandler())  # defaults to stderr
    logger.setLevel(logging.INFO)
    logger.info('1. This should appear just once on stderr.')
    logger.debug('2. This should not appear.')

    with logify(logger, level=logging.DEBUG):
        logger.debug('3. This should appear once on stderr.')

    logger.debug('4. This should not appear.')

    some_func()

    h = logging.StreamHandler(sys.stdout)
    with logify(logger, level=logging.DEBUG, handler=h, close=True):
        logger.debug(
            '5. This should appear twice - once on stderr and once on stdout.')

    logger.info('6. This should appear just once on stderr.')
logger.debug('7. This should not appear.')
