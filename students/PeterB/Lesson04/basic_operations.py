import peewee
import logging

LOG_FORMAT = "%(asctime)s %(filename)s:%(lineno)-3d %(levelname)s %(message)s"
LOG_FILE = 'db.log'

FORMATTER = logging.Formatter(LOG_FORMAT)
FILE_HANDLER = logging.FileHandler(LOG_FILE, mode='w')
FILE_HANDLER.setFormatter(FORMATTER)

CONSOLE_HANDLER = logging.StreamHandler()

CONSOLE_HANDLER.setFormatter(FORMATTER)

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger()
LOGGER.addHandler(FILE_HANDLER)
LOGGER.addHandler(CONSOLE_HANDLER)

database = peewee.SqliteDatabase("customers.db")
database.connect()
database.execute_sql('drop table if exists customer;')

class BaseModel(peewee, model):
    class Meta:
        database = database

class Customer(BaseModel):
    """
    Customer ID
    Name
    Lastname
    Home address
    Phone number
    Email address
    Status (active or inactive customer)
    Credit limit
    """

    customer_id = peewee.CharField(primary_key = True, max_length=30)
    name = peewee.CharField(max_length=50)
    last_name = peewee.CharField(max_length=50, null=True)
    home_address = peewee.CharField(max_length=75)
    phone_number = peewee.CharField(max_length=15)
    email = peewee.CharField(max_length=320)
    status = peewee.CharField(max_length=10) # "inACTIVE" or "active"
    credit_limit = peewee.CharField()


def add_customer(customer_id, name, last_name, home_address, phone_number, email, status, credit_limit):
    try:
        with database.transaction():
            Customer.create(
                customer_id=customer_id,
                name=name,
                Last_name=last_name,
                home_address=home_address,
                phone_number=phone_number,
                email=email,
                status=status,
                credit_limit=credit_limit
            )
            customer.save()
    except Exception as e:
        print(f"error creating {customer_id}")
        print(e)

def search_customers(customer_id):
    try:
        customer = Customer.get(customer.customer_id == customer_id)
        logging.info(f'Customer id {customer_id} found')
        return {
            "name": customer.name,
            "last_name": customer.last_name,
            "phone_number": customer.phone_number,
            "email_address": customer.email,
        }
    except Exception as e:
        LOGGER.warning(f"error reading customer {customer_id}")
        LOGGER.info(Exception)
        print(f"error reading customer {customer_id}")
        return{}


def delete_customer(customer_id):
    try:
        with database.transaction():
            customer = Customer.get(Customer.customer_id == customer_id)
            customer.delete_instance()
            customer.save()
            LOGGER.info('Customer ID %s has been deleted',
                        customer_id)
            return True
    except Exception as e:
        LOGGER.warning(f'Customer id {customer_id} Deletion was unsuccessful.')
        LOGGER.info(Exception)
        print("Failed to delete")
        print(e)
        return False


def update_customer_credit(customer_id, new_credit_limit):
    try:
        with database.transaction():
            customer_credit_update = Customer.get_by_id(customer_id)
            customer_credit_update.credit_limit = new_credit_limit
            customer_credit_update.save()
            LOGGER.info('Customer ID %s has been updated', customer_id)
    except Exception as e:
        LOGGER.warning(f'Customer id {customer_id} Credit limit update was unsuccessful.')
        LOGGER.info(Exception)
        print("Customer credit limit has updated")
        print(e)

def _list_active_customers():
    try:
        with database.transaction():
            customer_active = Customer.select().where(Customer.status == 'Active')
            LOGGER.info(f'Active customers: {customer_count}.')
    except Exception as e:
            LOGGER.warning(f'Unable to retrieve Active customers {customer_count}.')
            LOGGER.info(Exception)
            print('{} Active Customers'.format(len(customer_active)))
            return len(customer_active)

Customer.create_table()