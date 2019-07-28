"""
    Learning persistence with Peewee and sqlite
    delete the database to start over
        (but running this program does not require it)

    Person:

        1. filter records and display

"""
from personjob_modeli import *

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info('Working with Person class to search, find')

PERSON_NAME = 0
LIVES_IN_TOWN = 1
NICKNAME = 2

logger.info('Find and display by selecting with one Person name...')

aperson = Person.get(Person.person_name == 'Susan')
logger.info(f'{aperson.person_name} lives in {aperson.lives_in_town} ' + \
    f' and likes to be known as {aperson.nickname}')

logger.info('Search and display Person with missing nicknames')
logger.info('Our person class inherits select(). Specify search with .where()')
logger.info('Peter gets a nickname but noone else')

for person in Person.select().where(Person.nickname == None):
    logger.info(f'{person.person_name} does not have a nickname; see: {person.nickname}')
    if person.person_name == 'Peter':
        logger.info('Changing nickname for Peter')
        logger.info('Update the database')
        person.nickname = 'Painter'
        person.save()
    else:
        logger.info(f'Not giving a nickname to {person.person_name}')

logger.info('And here is where we prove it by finding Peter and displaying')
aperson = Person.get(Person.person_name == 'Peter')
logger.info(f'{aperson.person_name} now has a nickname of {aperson.nickname}')


database.close()
