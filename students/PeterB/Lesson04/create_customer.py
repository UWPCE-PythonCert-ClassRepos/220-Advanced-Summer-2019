import logging
from basic_operations import *

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)

LOGGER.info('Build the classes from the model in the database.')

DATABASE.create_tables([Customer])
DATABASE.close()