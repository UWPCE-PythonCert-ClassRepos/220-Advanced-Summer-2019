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
    job_name = CharField(primary_key=True, max_length=30)
    start_date = DateField(formats = 'YYYY-MM-DD')
    end_date = DateField(formats = 'YYYY-MM-DD')
    salary = DecimalField(max_digits = 7, decimal_places=2)
    person_employed = ForeignKeyField(Person, related_name='was_filled_by', null=False)


class PersonNumKey(BaseModel):
    person_name = CharField(max_length=30)
    lives_in_town = CharField(max_length=40)
    nickname = CharField(max_length=20, null=True)


database.execute_sql('drop table if exists job;')
database.execute_sql('drop table if exists person;')
database.execute_sql('drop table if exists personnumkey;')

Person.create_table()
Job.create_table()
PersonNumKey.create_table()

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
                    nicename = person[2],
                )
            print("Success, person added")
    except Exception as e:
        print(f'Error creating {person[0]}')
        print(e)


for person in Person:
    print(f'{person.person_name} lives in {person.lives_in_town} and likes to be known as {person.nickname}')


"""
NOTES FROM CLASS
"""
"""
CRUD
- Create
- Read
- Update
- Delete
"""

# Delete a person if they don't have a job
try:
    with database.transaction():
        job = Job.get(Job.person_employed == 'Andrew')
        job.delete_instance()

    with database.transaction():
        person = Person.get(Person.person_name == "Andrew")
        person.delete_instance()

except Exception as e:
    print('delete failed because Andrew has Jobs')
    print(f'Delete failed: {person.person_name}')
    print(e)
