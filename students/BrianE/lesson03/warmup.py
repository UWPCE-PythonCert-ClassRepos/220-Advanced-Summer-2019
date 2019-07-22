from peewee import *

database = SqliteDatabase("demo.db")
database.connect()
database.execute_sql("PRAGMA foreign_keys=ON;")


class BaseModel(Model):
    class Meta:
        database = database


class Person(BaseModel):
    person_name = CharField(primary_key=True, max_length=30)
    lives_in_town = CharField(max_length=50)
    nickname = CharField(max_length=20, null=True)


class Job(BaseModel):
    """
    This class defines Job, which maintains details of past Jobs held by a person
    """
    job_name = CharField(primary_key=True, max_length=30)
    start_date = DateField(formats='YYYY-MM-DD')
    end_date = DateField(formats='YYYY-MM-DD')
    salary = DecimalField(max_digits=7, decimal_places=2)
    person_employed = ForeignKeyField(Person, related_name='was_filled_by', null=False)


class PersonNumKey(BaseModel):
    """
    This class defines Person, which maintains details of someone for whom we
    want to research career to date.
    """
    person_name = CharField(max_length = 30)
    lives_in_town = CharField(max_length=40)
    nickname = CharField(max_length=20, null=True)


database.execute_sql('drop table if exists job;')
database.execute_sql('drop table if exists person;')
database.execute_sql('drop table if exists personnumkey;')

Person.create_table(Person)
Job.create_table(Job)


people = [
    ('Andrew', 'Sumner', 'Andy'),
    ('Peter', 'Seattle', None),
    ('Susan', 'Boston', 'Beannie'),
    ('Pam', 'Coventry', 'PJ'),
    ('Steven', 'Colchester', None),
]

for person in people:
    try:
        with database.transaction():
            new_person = Person.create(
                person_name = person[0],
                lives_in_town = person[1],
                nickname= person[2]
            )
        print(f'Person added: {person[0]}')
    except Exception as e:
        print(f'Error creating {person[0]}: {e}')


query = (
    Person
        .select(Person, Job)
        .join(Job, JOIN.INNER)
)

for person in query:
    print(f'Person {person.person_name} had job {person.job.job_name} starting on {person.job.start_date}')


try:
    with database.transaction():
        person = Person.get(Person.person_name == 'Andrew')
        person.delete_instance()
        print(f'Deleted {person.person_name}')
except Exception as e:
    print('Delete failed because Andrew has jobs')
    print(f'Delete failed: {person.person_name}')
    print(e)
