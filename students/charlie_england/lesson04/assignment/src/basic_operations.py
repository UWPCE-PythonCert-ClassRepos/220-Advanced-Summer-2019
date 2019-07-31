import peewee
import logging

logging.basicConfig(filename='basic_operations.log', filemode='w', format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S',level='DEBUG')

database = peewee.SqliteDatabase("customers.db")
database.connect()
database.execute_sql('drop table if exists customer;')

class BaseModel(peewee.Model):
    class Meta:
        database = database

class Customer(BaseModel):
    """
        This class defines Customer, which maintains details of someone
        for whom we want to research consumer habits to date.

        Customer ID
        Name
        Lastname
        Home address
        Phone Number
        Email address
        Status (active or inactive customer)
        Credit Limit
    """

    customer_id = peewee.CharField(primary_key=True, max_length=30)
    name = peewee.CharField(max_length=50)
    lastname = peewee.CharField(max_length=50, null=True)
    address = peewee.CharField(max_length=75)
    phone_number = peewee.CharField(max_length=15)
    email = peewee.CharField(max_length=320)
    status = peewee.CharField(max_length=10)
    credit_limit = peewee.FloatField()

database.create_tables([Customer])

def add_customer(customer_id, name, lastname, address, phone_number, email, status, credit_limit):
    """
        adds a new customer to the database.
    """
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
            logging.info(f'Customer {customer_id}/{name} created and added to database')
    except Exception as e:
        logging.error(f'Could not add {customer_id} due to {e}')

def search_customer(customer_id):
    """
        searches for an active customer given a customer ID
        returns a dictionary of the name, lastname, phone number and email
        if customerID not found, returns an empty dictionary
    """
    try:
        customer = Customer.get(Customer.customer_id == customer_id)
        logging.info(f'Customer {customer_id} found, returning information')
        return {
            'name':customer.name,
            'lastname':customer.lastname,
            'phone_number':customer.phone_number,
            'email':customer.email,
            'credit_limit':customer.credit_limit,
        }
    except Exception as e:
        logging.info(f'Customer {customer_id} not found with error:{e}')
        return {}



def delete_customer(customer_id):
    """
        deletes the customer from the database
    """
    try:
        with database.transaction():
            cust = Customer.get_by_id(customer_id)
            cust.delete_instance()
        logging.info(f'Customer {customer_id} has been successfully deleted')
        return True
    except Exception as e:
        logging.error(f'Customer {customer_id} could not be deleted, error: {e}')

def update_customer_credit(customer_id, credit_limit):
    """
        given a customer id, updates the credit limit
    """
    try:
        with database.transaction():
            cust = Customer.get_by_id(customer_id)
            cust.credit_limit = credit_limit
            cust.save()
        logging.info(f'Customer {customer_id} has been updated with a new {credit_limit} credit limit')
    except Exception as e:
        logging.error(f'Could not update credit limit for {customer_id} due to error: {e}')
        raise ValueError('NoCustomer')

def list_active_customers():
    """
        will return an integer with the number of active customers
        active customers have a status of active
    """
    try:
        count = Customer.select().where(Customer.status == 'active').count()
        logging.info(f'Collected information on active customers, currently {count} active customers')
        return count
    except Exception as e:
        logging.error(f'Could not return list of customers that are active due to {e}')

def mass_increase_credit_limit(limit_base=500,increase_by=1.2):
    """
        will take a variable (limit_base) and increase_by.
        will iterate through the current list of customers and increase everyone that is at or above limit_base
        will increase their credit limit by 1.2 or whatever number is given here
    """
    try:
        with database.transaction():
            customers = iter(Customer.select().where(Customer.credit_limit>=500))
            for customer in customers:
                if customer.status == 'active':
                    customer.credit_limit = customer.credit_limit*increase_by
                    customer.save()
            logging.info(f'all customers with {limit_base} credit limit or higher increased by {increase_by}')
    except Exception as e:
        logging.error('Error updating credit limit')