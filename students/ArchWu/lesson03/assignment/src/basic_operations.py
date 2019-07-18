"""
    Norton Furniture project
    store details of customers
    store and retrieve a customer’s credit limit
    produce monthly counts of the total number of active customers
"""
from peewee import *

database = SqliteDatabase("customers.db")
database.connect()
database.execute_sql('drop table if exists customer;')

class BaseModel(Model):
    class Meta:
        database = database




class Customer(BaseModel):
    """Customer database init"""
    customer_id = CharField(primary_key=True, max_length=30)
    name = CharField(max_length=50)
    lastname = CharField(max_length=50, null=False)
    address = CharField(max_length=75)
    phone_number = CharField(max_length=15)
    email = CharField(max_length=320)
    status = CharField(max_length=10)
    credit_limit = FloatField()

database.create_tables([Customer])

def add_customer(customer_id, name, lastname, address, phone_number, email, status, credit_limit):
    """add a customer"""
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

    except Exception as e:
        print(e)

def delete_customer(customer_id):
    """Delete a customer of given customer_id"""
    Customer.delete().where(Customer.customer_id == customer_id).execute()

def search_customers(customer_id):
    """Returns the customer of given customer_id"""
    try:
        customer = Customer.get(Customer.customer_id == customer_id)
        return customer
    except:
        pass

def update_customer_credit(customer_id, credit_limit):
    """Update the credit_limit of customer of given customer_id"""
    Customer.update(credit_limit=credit_limit).where(Customer.customer_id == customer_id).execute()
    return

def list_active_customers():
    """Returns the number of customer that has an active status"""
    return Customer.select().where(Customer.status == 'active').count()


