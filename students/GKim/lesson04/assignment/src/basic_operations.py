"""
    Create database example with Peewee ORM, sqlite and Python
"""
import logging
import datetime
from peewee import OperationalError, DoesNotExist
from customer_model import Customer, DATABASE
# noqa # pylint: disable=unused-import,too-few-public-methods,too-many-arguments, broad-except

LOG_FORMAT = "%(asctime)s %(filename)s:%(lineno)-3d %(levelname)s \
                %(message)s"

FORMATTER = logging.Formatter(LOG_FORMAT)

LOG_FILE = datetime.datetime.now().strftime("%Y-%m-%d-")+"db.log"
FILE_HANDLER = logging.FileHandler(LOG_FILE)
FILE_HANDLER.setFormatter(FORMATTER)
FILE_HANDLER.setLevel(logging.INFO)

CONSOLE_HANDLER = logging.StreamHandler()
CONSOLE_HANDLER.setLevel(logging.DEBUG)
CONSOLE_HANDLER.setFormatter(FORMATTER)
LOGGER = logging.getLogger()
LOGGER.addHandler(FILE_HANDLER)

LOGGER.info('One off program to build the classes from the model in \
            the database')

DATABASE.create_tables([
    Customer
    ])

DATABASE.close()

CUSTOMERS = [
    (1, 'Allen', 'Iverson', 'Philadelphia', '555-123-4567',
     'ai@gmail.com', True, 2000),
    (2, 'Shaw', 'Kemp', 'Seattle', '123-512-3568',
     'rainman@gmail.com', True, 1000),
    (3, 'Vince', 'Carter', 'Torento', '236-123-4569',
     'highligher@gmail.com', True, 5000),
    (4, 'Rose', 'Derrick', 'Chicago', '854-123-4570',
     'gDog@gmail.com', False, 2000),
    (5, 'Steve', 'Nash', 'Phoenix', '654-568-4961',
     'thehair@gmail.com', False, 100),
    ]


def add_toy_customers():
    '''
    This function will add make-up customers to the sqlite3 database for
    testing.
    '''
    delete_all_customers()

    for customer in CUSTOMERS:
        add_customer(*customer)


def print_customers():
    '''
    This function will print all customers in the sqlite3 database
    '''
    customers = return_all_customers()
    for customer in customers.dicts():
        print(customer)


def add_customer(customer_id, name, lastname, home_address, phone_number,
                 email_address, status, credit_limit):
    '''
    This function will add a new customer to the sqlite3 database.
    '''
    try:
        # id is automatically created and incremented by 1
        with DATABASE.transaction():
            new_customer = Customer.create(
                id=customer_id, name=name, last_name=lastname,
                home_address=home_address, phone_number=phone_number,
                email=email_address, status=status, credit_limit=credit_limit)
            new_customer.save()
            LOGGER.info(f'Database add successful for customerId {name}')

    except (OperationalError,
            DoesNotExist) as exc:
        LOGGER.info(f'Error creating = {name}')
        LOGGER.info(exc)


def return_all_customers():
    '''
    This function will return all customers object with name,
    lastname, email address and phone number of a customer or an empty
    dictionary object if no customer was found.
    '''

    LOGGER.info(f'REturn all customers')
    customers = Customer.select().where(Customer.id > 0)
    return customers


def search_customer(customer_id):
    '''
    This function will return a dictionary object with name,
    lastname, email address and phone number of a customer or an empty
    dictionary object if no customer was found.
    '''

    LOGGER.info(f'Search customer by Id: {customer_id}')
    acustomer = Customer.select().where(Customer.id == customer_id)
    if acustomer.exists():
        acustomer = acustomer.dicts().get()
    else:
        acustomer = None
    return acustomer


def delete_all_customers():
    '''
    This function will delete all customers from the sqlite3 database.
    '''
    d_cust = Customer.delete()
    d_cust.execute(DATABASE)
    LOGGER.info(f'We will delete all customers...')


def delete_customer(customer_id):
    '''
    This function will delete a customer from the sqlite3 database.
    '''
    acustomer = Customer.get(Customer.id == customer_id)
    LOGGER.info(f'We will delete this customer {customer_id}...')

    acustomer.delete_instance()


def update_customer_credit(customer_id, credit_limit):
    '''
    This function will search an existing customer by customer_id and update
    their credit limit or raise a ValueError exception if
    the customer does not exist.
    '''

    LOGGER.info(f'We will update this customer {customer_id}...')

    try:
        acustomer = Customer.get(Customer.id == customer_id)
        acustomer.credit_limit = credit_limit
        acustomer.save()
    except DoesNotExist:
        raise ValueError(f"Customer Id {customer_id} not found")


def list_active_customers():
    '''
    This function will return an integer with the number of customers
    whose status is currently active.
    '''
    count = Customer.select().where(Customer.status == 'Active').count()

    LOGGER.info('integer with the number of customers whose status is \
        currently active')

    return count