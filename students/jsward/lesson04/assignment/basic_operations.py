# They are not, in fact, constants...
# pylint: disable=C0103
# Seems to be a pylint false positive?
# pylint: disable=E1120
# Unfortunately the peewee documentation isn't very good about documenting it's exceptions :(
# pylint: disable=W0703
"""
basic_operations.py Lesson 4 edition

peewee
# model = table
# field instance = column
# model instance = row
"""

import logging
import datetime
import sys
import peewee

log_format = "%(asctime)s\t%(message)s"
formatter = logging.Formatter(log_format)

file_handler = logging.FileHandler("db_{}.log".format(datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")))
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(formatter)

logger = logging.getLogger(__name__)
logger.setLevel('INFO')
logger.addHandler(stream_handler)
logger.addHandler(file_handler)

customer_db = peewee.SqliteDatabase("customers.db")


class BaseModel(peewee.Model):
    """peewee base model"""
    class Meta:
        """Inner class"""
        # database is a keyword and must be set
        database = customer_db


class Customer(BaseModel):
    """Defines the Customer model (table)"""
    customer_id = peewee.CharField(primary_key=True, max_length=30)
    name = peewee.CharField(max_length=50)
    lastname = peewee.CharField(max_length=50, null=True)
    homeaddress = peewee.CharField(max_length=75)
    phone_number = peewee.CharField(max_length=15)
    email = peewee.CharField(max_length=320)
    status = peewee.CharField(max_length=15)
    credit_limit = peewee.FloatField()


customer_db.connect()
customer_db.execute_sql('drop table if exists customer;')
customer_db.create_tables([Customer])


def add_customer(customer_id, name, lastname, homeaddress, phone_number, email, status, credit_limit):
    """Adds customer to DB"""
    try:
        with customer_db.transaction():
            new_customer_mi = Customer.create(
                customer_id=customer_id,
                name=name,
                lastname=lastname,
                homeaddress=homeaddress,
                phone_number=phone_number,
                email=email,
                status=status,
                credit_limit=credit_limit
            )
            logger.debug("Added customer %s to %s", new_customer_mi, customer_db.database)
            return new_customer_mi
    except Exception as e:
        logger.error("Error creating customer_id %s: %s", customer_id, e)


def delete_customer(customer_id):
    """Deletes customer from DB"""
    try:
        with customer_db.transaction():
            del_result = Customer.delete().where(Customer.customer_id == customer_id).execute()
            if del_result == 1:
                logger.info("Successfully deleted customer ID %s", customer_id)
                return True
            logger.error("Failed to delete customer ID %s", customer_id)
            return False
    except Exception as e:
        logger.error("Error deleting customer ID %s: %s", customer_id, e)


def list_active_customers():
    """Lists active customers"""
    try:
        with customer_db.transaction():
            # Pylint false positive, Customer.select() definitely returns something ;)
            return len(Customer.select().where(
                (Customer.status == 'active') | (Customer.status == 'Active')))  # pylint: disable=E1111
    except Exception as e:
        print("Error listing active customers: {}".format(e))


def search_customer(customer_id):
    """Searches DB for customer_id"""
    try:
        with customer_db.transaction():
            search_result = Customer.select().where(Customer.customer_id == customer_id).get()
            if search_result:
                return {
                    "name": search_result.name,
                    "lastname": search_result.lastname,
                    "phone_number": search_result.phone_number,
                    "email": search_result.email,
                    "status": search_result.status,
                    "credit_limit": search_result.credit_limit
                }
            return {}
    except Customer.DoesNotExist as e:
        print("Error retrieving {}: {}".format(customer_id, e))
        return {}


def update_customer_credit(customer_id, credit_limit):
    """Updates the credit_limit of customer_id"""
    try:
        with customer_db.transaction():
            customer = Customer.select().where(Customer.customer_id == customer_id).get()
            customer.credit_limit = credit_limit
            customer.save()
            logger.info("Updated credit limit of customer ID %s to %s", customer_id, credit_limit)
    except Customer.DoesNotExist as e:
        logger.error("Error updating credit limit for customer %s: %s", customer_id, e)
        # Absolutely could not get pylint to recognize peewee's DoesNotExist error type, so raise ValueError instead
        raise ValueError("NoCustomer")


def populate_table_from_csv(csv_file, csv_encoding='iso-8859-15'):
    """Populates table from CSV file"""
    try:
        with open(file=csv_file, mode='r', encoding=csv_encoding) as input_file:
            # Could find a good place to add iterators/generators/comprehensions elsewhere, so made a new function
            # Also, yet another pylint false positive.  The below line isn't supposed to be assigned to anything.
            [add_customer(*l.split(',')) for l in input_file if 'Id,Name,Last_name,' not in l]  # pylint: disable=W0106
    except Exception as e:
        logger.error("Failed to load records from csv file %s into database %s: %s", csv_file, customer_db.database, e)


if __name__ == '__main__':
    pass
