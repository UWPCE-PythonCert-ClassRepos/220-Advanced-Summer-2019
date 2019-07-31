from peewee import *

database = SqliteDatabase('demo.db')
database.connect()
database.execute_sql("PRAGMA Foreign_keys=ON;")

class BaseModel(Model):
    class Meta:
        database = database

class Person(BaseModel):
    person_name = CharField(primary_key=True, max_length=30)
    lives_in_town = CharField(max_length=50)
    nickanme = CharField(max_length=20, null=True)

class Job(BaseModel):
    """"""
        this class defines Job, which maintains details of past jobs held by person
    """"""
    job_name = CharField(primary_key = True, max_legnth = 30)
    start_date = DateField(format = 'YYY-MM-DD')
    end_date = DateField(format = 'YYY-MM-DD')
    salary = DecimalField(max_digits = 7, decimal_places = 2)
    person_employed = ForeignKeyField(Person, related_name='was_filled_by', null = False)

class PersonNumKey(dataModel):
    person_nam = CharField(max_legnth = 30)
    lives_in_town = CharField(max_length = 40)
    nickname = CharField(max_length = 20. null = True)

database.execute_sql('drop table if exists job;')
database.execute_sql('drop table if exists person;')
database.execute_sql('drop table if exists personnumkey;')

person.create_table()
job.create_table()
PersonNumKey.create_table()


people = [
    ('Andre', 'Summer', 'Andy'),
    ('Peter', 'Seattle', 'None'),
    ('Susan', 'Boston', 'Beannie'),
    ('Pam', 'New York', 'None')
]

for person in people:
    try:
    with database.transaction(
        new_person = Person.create[]
            person_name = person[0]
            lives_in_town = person[1]
            nickname = person[2],
            )
            print("success, person added")
    except Exception as e:
        print(f'Error creating {person[0]}')

query
