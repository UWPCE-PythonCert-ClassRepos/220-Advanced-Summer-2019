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
    This class defines Job, Which mantains details of past Jobs
    held by a Person
    """

    job_name = CharField(primary_key=True, max_length=30)
    start_date = DateField(formats= "YYYY-MM-DD")
    end_date = DateField(formats= "YYYY-MM-DD")
    salary = DecimalField(max_digits=7, decimal_places=2)
    perosn_employed = ForeignKeyField(Person, related_name="was_filled_by", null=False)

class PersonNumKey(BaseModel):
    """
    This class defines Person which maintains details of someone
    for whome we want to research career to date.
    """
    person_name = CharField(max_length=30)
    lives_in_town = CharField(max_length=40)
    nickname = CharField(max_length=20, null=True)


database.execute_sql("drop table if exits job;")
database.execute_sql("drop table if exits person;")
database.execute_sql("drop table if exits personnumkey;")

Person.create_table()
Job.create_table()
PersonNumKey.create_table()

people = [
    ("Andrew", "Sumner", "Andy"),
    ("Peter", "Seattle", None),
    ("Susan", "Boston", "Beannie"),
    ("Pam", "Conventry", "PJ"),
    ("Steven", "Colchester", None),
    ]

for person in people:
    try:
        with database.transaction():
            new_person = Person.create(
                person_name = person[0],
                lives_in_town = person[1],
                nickname = person[2],
            )
            print("sucess, person added")
    except Exception as e:
        print(f'Error creating {person[0]}')
        print(e)

for person in Person:
    print(f'{person.person_name} lives in {person.lives_in_town}')