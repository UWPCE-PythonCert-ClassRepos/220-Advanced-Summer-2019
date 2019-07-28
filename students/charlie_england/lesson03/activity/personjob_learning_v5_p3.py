"""
    Learning persistence with Peewee and sqlite
    delete the database to start over
        (but running this program does not require it)


"""

from personjob_modeli import *

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info('View matching records and Persons without Jobs (note LEFT_OUTER)')


query = (Person
         .select(Person, Job)
         .join(Job, JOIN.LEFT_OUTER)
        )

for person in query:
    try:
        logger.info(f'Person {person.person_name} had job {person.job.job_name}')

    except Exception as e:
        logger.info(f'Person {person.person_name} had no job')

logger.info('Example of how to summarize data')
logger.info('Note select() creates a count and names it job_count')
logger.info('group_by and order_by control level and sorting')

query = (Person
         .select(Person, fn.COUNT(Job.job_name).alias('job_count'))
         .join(Job, JOIN.LEFT_OUTER)
         .group_by(Person)
         .order_by(Person.person_name))

for person in query:
    logger.info(f'{person.person_name} had {person.job_count} jobs')


database.close()
