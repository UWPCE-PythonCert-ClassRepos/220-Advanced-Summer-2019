""" DATABASE assignment """

import logging
import peewee

DATABASE = peewee.SqliteDatabase('customers.db')
# DATABASE.execute_sql('PRAGMA foreign_keys=ON;')
DATABASE.connect()
DATABASE.execute_sql('drop table if exists customer;')


# Logging just for fun
LOG_FILE = "DATABASE_logs.log"
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
        DATABASE = DATABASE


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


DATABASE.create_tables([Customer])


# Complete
def add_customer(customer_id, name, lastname, address, phone_number, email, status, credit_limit):
    """ Add a customer to the database """

    try:
        with DATABASE.transaction():
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
            logging.error(f"Successfully saved {customer_id} to DATABASE")

    except:
        logging.error(f"Error creating {customer_id}")
    finally:
        logging.error('DATABASE closed')
        DATABASE.close()


# Complete
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

    except ValueError:
        print(f"error reading customer {customer_id}")
        return {}


def delete_customer(customer_id):
    """ Delete a customer from the database """

    try:
        with DATABASE.transaction():
            customer = Customer.get(Customer.customer_id == customer.id)
            customer.delete()
            logging.error(f"{customer.id} has been removed")
    except ValueError:
        logging.error(f"Unable to delete user {customer_id}")
    finally:
        DATABASE.close()


def update_customer_credit(customer_id, credit_limit):
    """ Update a customer from the database """

    try:
        with DATABASE.transaction():
            customer_to_update = Customer.get(Customer.customer_id == customer.id)
    except ValueError:
        logging.error(f"Unable to update user, {customer_id}")
    finally:
        DATABASE.close()


# Complete
def list_active_customers():
    """ List all active customers in the database """

    try:
        count_customer = Customer.get(Customer.customer_id == customer_id)
        return len(count_customer)
    except ValueError:
        logging.error("Unable to count users in DATABASE")
        print("Unable to count")
    finally:
        DATABASE.close()
