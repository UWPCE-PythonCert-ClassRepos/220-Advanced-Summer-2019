"""
    Norton Furniture project
    store details of customers
    store and retrieve a customer’s credit limit
    produce monthly counts of the total number of active customers
"""
import logging
import peewee

logging.basicConfig(filename='basic.log', filemode='w',
                    format='%(asctime)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S',
                    level='DEBUG')
database = peewee.SqliteDatabase("customers.db")
database.connect()
database.execute_sql('drop table if exists customer;')

class BaseModel(peewee.Model):
    """Init of base model"""
    class Meta:
        """Init of Meta class"""
        database = database

class Customer(BaseModel):
    """Customer database init"""
    customer_id = peewee.CharField(primary_key=True, max_length=30)
    name = peewee.CharField(max_length=50)
    lastname = peewee.CharField(max_length=50, null=False)
    address = peewee.CharField(max_length=75)
    phone_number = peewee.CharField(max_length=15)
    email = peewee.CharField(max_length=320)
    status = peewee.CharField(max_length=10)
    credit_limit = peewee.FloatField()

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
            logging.info("added customer %s", customer_id)

    except Exception as e:
        logging.error("Error adding customer %s", customer_id)

def delete_customer(customer_id):
    """Delete a customer of given customer_id"""
    if search_customer(customer_id) != {}:
        Customer.delete().where(Customer.customer_id == customer_id).execute()
    else:
        logging.warning("No customer is deleted since non-exist")
    # debug_ = search_customer(customer_id)
    # logging.debug(debug_)
    return True

def search_customer(customer_id):
    """Returns the customer of given customer_id"""
    try:
        customer = Customer.get(Customer.customer_id == customer_id)
        return {
            'name':customer.name,
            'lastname':customer.lastname,
            'phone_number':customer.phone_number,
            'email':customer.email,
            'status':customer.status,
            'credit_limit':customer.credit_limit
        }
    except Exception as e:
        logging.error("Error when finding customer %s due to %s", customer_id, e)
        return {}

def update_customer_credit(customer_id, credit_limit):
    """Update the credit_limit of customer of given customer_id"""
    if search_customer(customer_id) != {}:
        try:
            customer = Customer.update(credit_limit=credit_limit).where(Customer.customer_id == customer_id).execute()
            return customer
        except ValueError as e:
            logging.error("Error updating customer %s due to %s", customer_id, e)
    else:
        logging.error("No customer found!")

def list_active_customers():
    """Returns the number of customer that has an active status"""
    return Customer.select().where(Customer.status == 'active').count()
