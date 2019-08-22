"""
Copied and Pasted from Lesson03.

New goal is to refactor this assignment and incorporate the following:

comprehensions
generators
iterators
iterables



"""

import peewee

database = peewee.SqliteDatabase("customers.db")
database.connect()

database.execute_sql('PRAGMA foreign_keys = ON;')
database.execute_sql('drop table if exists customer;')


# the string below could be added to the execute_sql call for a specific call
# 'PRAGMA foreign_keys = ON'

# fred = Customer.get
# fred = Customer.delete_instance()

class Basemodel(peewee.Model):
    class Meta:
        database = database


class Customer(Basemodel):
    """
    Customer ID.
    Name.
    Lastname.
    Home address.
    Phone number.
    Email address.
    Status (active or inactive customer).
    Credit limit.
    """
    customer_id = peewee.CharField(primary_key=True, max_length=30)
    name = peewee.CharField(max_length=50)
    lastname = peewee.CharField(max_length=50, null=True)
    address = peewee.CharField(max_length=75)
    phone_number = peewee.CharField(max_length=15)
    email = peewee.CharField(max_length=320)
    status = peewee.CharField(max_length=10)
    credit_limit = peewee.FloatField()


Customer.create_table()  # from peewee


def add_customer(customer_id, name, lastname, address, phone_number, email, status, credit_limit):
    try:
        with database.transaction():
            customer = Customer.create(
                customer_id=customer_id,
                name=name,
                lastname=lastname,
                address=address,
                phone_number=phone_number,
                email=email,
                status=status,
                credit_limit=credit_limit,
            )
            customer.save()

    except Exception as e:
        print(f'error creating {customer_id}')
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
        print(f'error creating {customer_id}')
        return {}


def delete_customer(customer_id):
    try:
        with database.transaction():
            customer = Customer.get(Customer.customer_id == customer_id)  # class
            customer.delete_instance()  # class
            customer.save()  # class
            return True
    except Exception as e:
        print(e)
        return False  # class


def update_customer_credit(customer_id, credit_limit):
    try:
        with database.transaction():
            customer = Customer.get(Customer.customer_id == customer_id)  # class
            customer.credit_limit = credit_limit

            customer.save()  # class

    except:
        raise ValueError('NoCustomer')


def list_active_customers():  # akin to search_customer
    try:
        print(Customer.select())

        return Customer.select().where(Customer.status == 'active').count()
    except Exception as e:
        print(e)
