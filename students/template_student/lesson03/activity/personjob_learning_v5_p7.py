"""
    Learning persistence with Peewee and sqlite
    delete the database to start over
        (but running this program does not require it)


"""
from personjob_modeli import *

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("Back to Person class: try to change Peter's name")

aperson = Person.get(Person.person_name == 'Peter')
logger.info(f'Current value is {aperson.person_name}')

logger.info('Update Peter to Peta, thereby trying to change the PK...')

try:
    with database.transaction():
        aperson = Person.get(Person.person_name == 'Peter')
        aperson.person_name = 'Peta'
        aperson.save()
        logger.info(f'Tried to change Peter to {aperson.person_name}')

except Exception as e:
    logger.info(f'Cant change a PK and caught you trying') # not caught; no error thrown by Peewee
    logger.info(e)

aperson = Person.get(Person.person_name == 'Peter')
logger.info(f'Looked for Peter: found! -> {aperson.person_name}')

try:
    aperson = Person.get(Person.person_name == 'Peta')

except Exception as e:
    logger.info(f'Looking for Peta results in zero records. PK changes are ignored and do not throw an error!!!!')
    logger.info(f'Cant change a PK')
    logger.info('PK "change" can only be achieved with a delete and new create')

database.close()
