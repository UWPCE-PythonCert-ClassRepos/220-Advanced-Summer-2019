"""
    Learning persistence with Peewee and sqlite
    delete the database to start over
        (but running this program does not require it)


"""

from personjob_modeli import *

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info('Working with Job class')

logger.info('Example of how to summarize data. Also shows join)')
logger.info('Note how we generate the count in the select()')
logger.info('group_by and order_by control the level of totals and sorting')


logger.info('Try to add a new job where a person doesnt exist...')

JOB_NAME = 0
START_DATE = 1
END_DATE = 2
SALARY = 3
PERSON_EMPLOYED = 4

addjob = ('Sales', '2010-04-01', '2018-02-08', 80400, 'Harry')

logger.info('We are trying to add:')
logger.info(addjob)

try:
    with database.transaction():
        new_job = Job.create(
                job_name = addjob[JOB_NAME],
                start_date = addjob[START_DATE],
                end_date = addjob[END_DATE],
                salary = addjob[SALARY],
                person_employed = addjob[PERSON_EMPLOYED])
        new_job.save()

except Exception as e:
    logger.info('But we get an exception')
    logger.info(f'For Job create: {addjob[0]}')
    logger.info(e)

logger.info('Try to Delete a person who has jobs...')

try:
    with database.transaction():
        aperson = Person.get(Person.person_name == 'Andrew')
        logger.info(f'Trying to delete {aperson.person_name} who lives in {aperson.lives_in_town}')
        aperson.delete_instance()

except Exception as e:
    logger.info(f'Delete failed: {aperson.person_name}')
    logger.info(e)


database.close()
