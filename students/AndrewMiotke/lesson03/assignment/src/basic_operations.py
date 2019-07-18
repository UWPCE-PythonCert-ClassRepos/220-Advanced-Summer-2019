""" Database assignment """

import peewee

database = peewee.SqliteDatabase('customers.db')
database.execute_sql('PRAGMA foreign_keys=ON;')
database.connect()

database.execute_sql('drop table if exists customer;')

class BaseModel(peewee.Model):
    class Meta:
        database = database

class Customer(BaseModel):

    customer_id = peewee.CharField(primary=True, max_length=30)
    name = peewee.CharField(max_length=50)
    lastname = peewee.CharField(max_length=50)
    address = peewee.CharField(max_length=75)
    phone_number = peewee.CharField(max_length=15)
    email = peewee.CharField(max_length=320)
    status = peewee.CharField(max_length=10)
    credit_limit = peewee.FloatField()


def add_customer(customer_id, name, lastname, address, phone_number, email, status, credit_limit):
    try:
        with database.transaction():
            Customer.create(
                customer_id = customer_id,
                name = name,
                lastname = lastname,
                address = address,
                phone_number = phone_number,
                email = email,
                status = status,
                credit_limit = credit_limit,
            )
            customer.save()
            # add logging to verify user was saved

    except Exception as e:
        print(f"error creating {customer_id}")
        print(e)


def search_customer(customer_id):
    try:
        customer = Customer.get(Customer.customer_id == customer_id)
        return {
            "name": customer.name,
            "lastname": customer.lastname,
            "phone_number": customer.phone_number,
            "email": customer.email,
        }

    except Exception as e:
        print(f"error reading customer {customer_id}")
        return {}


def delete_customer(customer_id):
    try:
        with database.transaction():
        #customer.delete()? This might work
    except Exception as e:
        print(e)


def update_customer_credit(customer_id, credit_limit):
    try:
        with database.transaction():
        pass
    except Exception as e:
        print(e)


def list_active_customers():
    pass