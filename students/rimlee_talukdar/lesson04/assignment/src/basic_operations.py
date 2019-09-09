"""
Basic operation of customer database
"""
import logging
import peewee

logging.basicConfig(filename='basic_operations.log',
                    filemode='w',
                    format='%(asctime)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S',
                    level='DEBUG')
__database__ = peewee.SqliteDatabase("customers.db")
__database__.connect()
__database__.execute_sql('drop table if exists customer;')

class BaseModel(peewee.Model):
    """
    Peewee base model
    """
    class Meta:
        """
        Meta field of the database
        """
        database = __database__


class Customer(BaseModel):
    """
    This is the customer model. Following model stores the following data
        customer_id field for Customer ID
        name field for Name
        lastname field for Lastname
        address field for Home address
        phone_number field for Phone Number
        email field for Email address
        status field for Status (active or inactive customer)
        credit_limit field for Credit Limit
    """

    customer_id = peewee.CharField(primary_key=True, max_length=30)
    name = peewee.CharField(max_length=50)
    lastname = peewee.CharField(max_length=50, null=True)
    address = peewee.CharField(max_length=75)
    phone_number = peewee.CharField(max_length=15)
    email = peewee.CharField(max_length=320)
    status = peewee.CharField(max_length=10)
    credit_limit = peewee.FloatField()


__database__.create_tables([Customer])


def add_customer(customer_id, name, lastname, address,
                 phone_number, email, status, credit_limit):
    """
    Adds customer to the database
    :param customer_id field for Customer ID
    :param name field for Name
    :param lastname field for Lastname
    :param address field for Home address
    :param phone_number field for Phone Number
    :param email field for Email address
    :param status field for Status (active or inactive customer)
    :param credit_limit field for Credit Limit
    :return: None
    """
    try:
        with __database__.transaction():
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
            logging.info(f'Added {customer_id}/{name} to the database')
    except Exception as exception:
        logging.error(f'Could not add {customer_id} due to:\n\t {exception}')


def search_customer(customer_id):
    """
    Searches for an active customer for a given customer ID
    :param customer_id is the Customer Id of the user
    :return: a dictionary of the name, lastname, phone number and email
    if customerID not found, returns an empty dictionary
    """
    try:
        customer = Customer.get(Customer.customer_id == customer_id)
        logging.info(f'Customer {customer_id} found, returning information')
        return {
            'name': customer.name,
            'lastname': customer.lastname,
            'phone_number': customer.phone_number,
            'email': customer.email,
        }
    except Exception as exception:
        logging.info(f'Customer {customer_id} not found with error:' +
                     f'\n\t{exception}')
        return {}


def delete_customer(customer_id):
    """
    Deletes the customer from the database
    :param customer_id of the customer
    :return: None
    """
    try:
        with __database__.transaction():
            cust = Customer.get_by_id(customer_id)
            cust.delete_instance()
        logging.info(f'Customer {customer_id} has been successfully deleted')
        return True
    except Exception as exception:
        logging.error(f'Customer {customer_id} could not be ' +
                      f'deleted due to\t\n{exception}')


def update_customer_credit(customer_id, credit_limit):
    """
    Updates the credit limit for a given customer id
    :param customer_id of the Customer
    :param credit_limit new credit limit
    :return: None
    """
    try:
        with __database__.transaction():
            cust = Customer.get_by_id(customer_id)
            cust.credit_limit = credit_limit
            cust.save()
        logging.info(f'New credit limit for customer {customer_id} is' +
                     f' {credit_limit}')
    except Exception as exception:
        logging.error(f'Could not update credit limit for {customer_id}'
                      f' due to:\n\t{exception}')
        raise ValueError


def list_active_customers():
    """
    Give list of active customer
    :return: an integer with the number of active customers
    """
    try:
        active_count = 0
        customers = iter(Customer.select().where(Customer.status == 'active'))
        for _ in customers:
            active_count += 1
        logging.info(f'Currently {active_count} active customers' +
                     f' exist in the system')
        return active_count
    except Exception as exception:
        logging.error(f'Could not return list of customers that are'+
                      f' active due to {exception}')
