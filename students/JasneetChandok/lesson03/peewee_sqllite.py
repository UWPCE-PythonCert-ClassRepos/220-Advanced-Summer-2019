from peewee import *

database = SqliteDatabase("demo.db")
database.connect
database.execute_sql("PRAGMA foreign_keys=ON;")


class BaseModel(Model):
    class Meta:
        database = database


class Person(BaseModel):
    person_name = CharField(primary_key=True, max_length=30)
    lives_in_Town = CharField(max_length=50)
    nickname = CharField(max_length=20, null=True)


class Job(BaseModel):
    job_name = CharField(primary_key=True, max_length=30)
    start_date = DateField(format='YYYY-MM-DD')
    end_date = DateField(formats='YYYY-MM-DD')
    salary = DecimalField(max_digits=7, decimal_places=2)
    person_employed = ForeignKeyField(Person, related_name='was_filled_by', null=False)


class PersonNumKey(BaseModel):
    person_name = CharField(max_length=30)
    lives_in_Town = CharField(max_length=40)
    nickname = CharField(max_length=20, null=True)


database.execute_sql('drop table if exists job;')
database.execute_sql('drop table if exists person;')
database.execute_sql('drop table if exits personnumkey')

Person.create_table()
Job.create_table()
PersonNumKey.create_table()

people = [
    ('Andrew', 'Summer', 'Andy'),
    ('Andrew', 'Summer', 'Andy'),
    ('Andrew', 'Summer', 'Andy')
]

for person in people:
    try:
        with database.transaction():
            new_person = Person.create(
                person_name=person[0],
                lives_in_Town=person[1],
                nickname=person[2],
            )
    except Exception as e:
        perint(f'Error createing {person[0]}')
        print(e)

'''Assignment'''

def add_customer(customer_id, name, lastname, address, phone_number,email, status, credit_limits):
    try:
        with database.transaction():
            Customer.create(
                customer_id=customer_id,
                name=name,
                lastname=lastname,
                address=address,
                phone_number=phone_number,
                email=email,
                status=status,
                credit_limits=credit_limits,
            )
        customer.save()
    except Exception as e:
        print('error creating{customer_id}')
        print(e)


def search_customer(customer_id):
    try:
        customer = Customer.get(Customer.customer_id == customer_id)
        return{
            "name": customer.name,
            "lastname": customer.lastname,
            "phone_number": customer.phone_number,
            "email": customer.email,
        }
    except Exception as e:
        print(f"error reading customer")
        # print(e)
        return{}
