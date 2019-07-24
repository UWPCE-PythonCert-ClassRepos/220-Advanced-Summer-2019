from peewee import *

database = SqliteDatabase("customers.db")
database.connect()
database.execute_sql("PRAGMA foreign_keys=ON;")


class BaseModel(Model):
    """
    Base peewee model class
    """

    class Meta:
        database = database


class Customer(BaseModel):
    """
    Customer class for storing customer details and credit limit
    """
    customer_id = IntegerField(primary_key=True)
    name = CharField(max_length=50)
    lastname = CharField(max_length=50)
    home_address = CharField(max_length=50)
    phone_number = CharField(max_length=50)
    email = CharField(max_length=50)
    status = CharField(max_length=10)
    credit_limit = IntegerField()


class CustomerDoesNotExist(Exception):
    """ Raise if searching for non-existent customer """
    pass


def add_customer(customer_id, name, lastname, home_address, phone_number, email, status, credit_limit):
    """
    Add a new customer to the sqlite3 database
    :param customer_id: integer
    :param name: string
    :param lastname: string
    :param home_address: string
    :param phone_number: string
    :param email: string
    :param status: string (Active/Inactive)
    :param credit_limit: float
    :return: None
    """
    try:
        with database.transaction():
            customer = Customer.create(
                customer_id=customer_id,
                name=name,
                lastname=lastname,
                home_address=home_address,
                phone_number=phone_number,
                email=email,
                status=status,
                credit_limit=credit_limit,
            )
            customer.save()
    except Exception as e:
        print(f'Error creating {customer_id}: {e}')


def search_customer(customer_id):
    """
    Return a dictionary object with name, lastname, email address and phone number
    of a customer or an empty dictionary object if no customer was found.
    :param customer_id: integer
    :return: dictionary
    """
    customer_details = {}
    try:
        customer = Customer.get(Customer.customer_id == customer_id)
        customer_details['name'] = customer.name
        customer_details['lastname'] = customer.lastname
        customer_details['phone_number'] = customer.phone_number
        customer_details['email'] = customer.email
    except CustomerDoesNotExist as e:
        print(f'Customer not found: customer_id: {customer_id} {e}')
    finally:
        return customer_details


def delete_customer(customer_id):
    """
    Delete a customer from the sqlite3 database.
    :param customer_id: integer
    :return: dictionary
    """
    try:
        with database.transaction():
            customer = Customer.get(Customer.customer_id == customer_id)
            customer.delete_instance()
            customer.save()
        return True
    except Exception:  # return empty dictionary if customer_id doesn't match
        return {}


def update_customer_credit(customer_id, credit_limit):
    """
    Search an existing customer by customer_id and update their credit limit
    or raise a ValueError exception if the customer does not exist.
    :param customer_id: integer
    :param credit_limit: float
    :return:
    """
    try:
        with database.transaction():
            customer = Customer.get(Customer.customer_id == customer_id)
            customer.update(Customer.credit_limit == credit_limit)
            customer.save()
    except Exception as e:
        raise ValueError(f"Customer does not exist. {e}")


def list_active_customers():
    """
    Return an integer with the number of customers whose status is currently active.
    :return: integer
    """
    query = (Customer.select().where(Customer.status == 'active').count())
    return query
