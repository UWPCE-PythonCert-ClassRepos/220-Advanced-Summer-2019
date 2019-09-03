"""
basic operations module
"""
import peewee

database = peewee.SqliteDatabase("customer.db")
database.connect()
database.execute_sql('drop table if exists customer;')


class BaseModel(peewee.Model):
    """
    Base model for database
    """
    class Meta:
        """
        database
        """
        database = database


class Customer(BaseModel):
    """
    Class defines Customer as stores their information
    """
    customer_id = peewee.CharField(primary_key=True, max_length=50)
    name = peewee.CharField(max_length=20)
    lastname = peewee.CharField(max_length=20, null=True)
    home_address = peewee.CharField(max_length=50)
    phone_number = peewee.CharField(max_length=30)
    email_address = peewee.CharField(max_length=100)
    status = peewee.CharField(max_length=10)
    credit_limit = peewee.FloatField()


database.create_tables([Customer])


def add_customer(customer_id, name, lastname, home_address,
                 phone_number, email_address, status, credit_limit):
    """
    This function will add a new customer to the sqlite3 database
    """
    try:
        with database.transaction():
            customer = Customer.create(
                customer_id=customer_id,
                name=name,
                lastname=lastname,
                home_address=home_address,
                phone_number=phone_number,
                email_address=email_address,
                status=status,
                credit_limit=credit_limit,
            )
            customer.save()
    except Exception as unknown_error:
        print(unknown_error)


def search_customer(customer_id):
    """
    This function will return a dictionary object with name,
    lastname, email address and phone number of a customer or
    an empty dictionary object if no customer was found
    """
    try:
        customer = Customer.get(Customer.customer_id == customer_id)
        return {
            'name': customer.name,
            'lastname': customer.lastname,
            'email_address': customer.email_address,
            'phone_number': customer.phone_number
        }
    except Exception as unknown_error:
        print(f"Error. Could not find customer {customer_id}. {unknown_error}")
        return {}


def delete_customer(customer_id):
    """
    This function will delete a customer from the sqlite3 database.
    """
    try:
        with database.transaction():
            customer = Customer.get(Customer.customer_id == customer_id)
            customer.delete_instance()
            customer.save()
    except Exception as unknown_error:
        print(f'Error. Could not delete customer {customer_id}. {unknown_error}')


def update_customer_credit(customer_id, credit_limit):
    """
    This function will search an existing customer by
    customer_id and update their credit limit or raise a
    ValueError exception if the customer does not exist.
    """
    try:
        with database.transaction():
            customer = Customer.get_by_id(customer_id)
            customer.credit_limit = credit_limit
            customer.save()
    except Exception as unknown_error:
        print(f'Error. Cutomer {customer_id} does not exist. {unknown_error}')
        raise ValueError


def list_active_customers():
    """
    This function will return an integer with the
    number of customers whose status is currently active.
    """
    try:
        active_customer_count = 0
        for _ in Customer.select().where(Customer.status == 'Active'):
            active_customer_count += 1
        return active_customer_count
    except Exception as unknown_error:
        print(f'Error. Not able to count number of active customers. {unknown_error}')
