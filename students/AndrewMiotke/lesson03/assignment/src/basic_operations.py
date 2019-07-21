""" Database assignment """

import peewee
import logging

database = peewee.SqliteDatabase('customers.db')
# database.execute_sql('PRAGMA foreign_keys=ON;')
database.connect()
database.execute_sql('drop table if exists customer;')


# Logging just for fun
LOG_FILE = "database_logs.log"
logger = logging.getLogger()
logger.setLevel(logging.ERROR)
LOG_FORMAT = "%(asctime)s\t %(filename)s: %(lineno)-3d %(levelname)s %(message)s)"
FORMATTER = logging.Formatter(LOG_FORMAT)

FILE_HANDLER = logging.FileHandler(LOG_FILE)
FILE_HANDLER.setFormatter(FORMATTER)

class BaseModel(peewee.Model):
    class Meta:
        database = database


class Customer(BaseModel):

    customer_id = peewee.CharField(primary_key=True, max_length=30)
    name = peewee.CharField(max_length=50)
    lastname = peewee.CharField(max_length=50)
    address = peewee.CharField(max_length=75)
    phone_number = peewee.CharField(max_length=15)
    email = peewee.CharField(max_length=320)
    status = peewee.CharField(max_length=10)
    credit_limit = peewee.FloatField()


database.create_tables([Customer])


# Complete
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
            logging.error(f"Successfully saved {customer_id} to database")

    except:
        logging.error(f"Error creating {customer_id}")


# Complete
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
            customer = Customer.get(Customer.customer_id == customer.id)
            customer.delete()
    except:
        logging.error(f"Unable to delete user {customer_id}")
        print(e)


def update_customer_credit(customer_id, credit_limit):
    try:
        with database.transaction():
            customer = Customer.get(Customer.customer.id == customer.id)
    except ValueError:
        logging.error(f"Unable to update user, {customer_id}")
        print(e)


def list_active_customers():
    try:
        count_customer = Customer.get(Customer.customer_id == customer_id)
        return len(count_customer)
    except ValueError:
        logging.error("Unable to count users in database")
        print("Unable to count")

