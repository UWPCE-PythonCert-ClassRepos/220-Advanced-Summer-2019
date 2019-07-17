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

JOB_NAME = 0
START_DATE = 1
END_DATE = 2
SALARY = 3
PERSON_EMPLOYED = 4

logger.info('Now resolve the join and print (INNER shows only jobs that match person)...')
logger.info('Notice how we use a query variable in this case')
logger.info('We select the classes we need, and we join Person to Job')
logger.info('Inner join (which is the default) shows only records that match')

query = (Person
         .select(Person, Job)
         .join(Job, JOIN.INNER)
        )

logger.info('View matching records from both tables')

for person in query:
    logger.info(f'Person {person.person_name} had job {person.job.job_name}')


database.close()
