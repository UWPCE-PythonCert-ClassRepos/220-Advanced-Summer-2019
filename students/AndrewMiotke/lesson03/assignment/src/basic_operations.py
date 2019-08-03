""" database assignment """

import logging
import peewee

database = peewee.SqliteDatabase('customers.db')
# database.execute_sql('PRAGMA foreign_keys=ON;')
database.connect()
database.execute_sql('drop table if exists customer;')


# Logging just for fun
LOG_FILE = "database_logs.log"
LOGGER = logging.getLogger()
LOGGER.setLevel(logging.ERROR)
LOG_FORMAT = "%(asctime)s\t %(filename)s: %(lineno)-3d %(levelname)s %(message)s)"
FORMATTER = logging.Formatter(LOG_FORMAT)

FILE_HANDLER = logging.FileHandler(LOG_FILE)
FILE_HANDLER.setFormatter(FORMATTER)

class BaseModel(peewee.Model):
    """ Base class for peewee and the sqlite3 database """

    class Meta:
        """ Peewee boilerblate """
        database = database


class Customer(BaseModel):
    """ Establish the datbase model """

    customer_id = peewee.CharField(primary_key=True, max_length=30)
    name = peewee.CharField(max_length=50)
    lastname = peewee.CharField(max_length=50)
    address = peewee.CharField(max_length=75)
    phone_number = peewee.CharField(max_length=15)
    email = peewee.CharField(max_length=320)
    status = peewee.CharField(max_length=10)
    credit_limit = peewee.FloatField()


database.create_tables([Customer])


def add_customer(customer_id, name, lastname, address, phone_number, email, status, credit_limit):
    """ Add a customer to the database """

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
                credit_limit=credit_limit,
                )
            customer.save()
            logging.error(f"Successfully saved {customer_id} to database")

    except:
        logging.error(f"Error creating {customer_id}")


def search_customer(customer_id):
    """ Search for customer in the database """

    try:
        customer = Customer.get(Customer.customer_id == customer_id)
        return {
            "name": customer.name,
            "lastname": customer.lastname,
            "phone_number": customer.phone_number,
            "email": customer.email,
        }

    except peewee.DoesNotExist:
        print(f"Error finding customer, {customer_id}")
        return {}


def delete_customer(customer_id):
    """ Delete a customer from the database """

    try:
        with database.transaction():
            customer = Customer.get(Customer.customer_id == customer_id)
            customer.delete_instance()
            logging.error(f"{customer.id} has been removed")
    except peewee.DoesNotExist:
        logging.error(f"Unable to delete user {customer_id}")


def update_customer_credit(customer_id, credit_limit):
    """ Update a customer from the database """

    try:
        with database.transaction():
            customer_to_update = Customer.update(Customer.credit_limit).where(Customer.credit_limit)
            customer_to_update.execute()
            customer_to_update.save()
    except peewee.DoesNotExist:
        logging.error(f"Unable to update user, {customer_id}")


def list_active_customers():
    """ List all active customers in the database """

    try:
        return Customer.select().where(Customer.status == 'active').count()
    except peewee.DoesNotExist:
        logging.error("Unable to count users in database")
        print("Unable to count")


"""
Used in the command line when viewing a SQlite database

$ sqlite3 customers.db
$ .tables # shows the tables
$ select * from customer # shows anything in the customer table

"""