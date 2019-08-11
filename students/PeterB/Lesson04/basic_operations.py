import peewee

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
    lastname = peewee.CharField(max_length=50, null=True)
    homeaddress = peewee.CharField(max_length=75)
    phonenumber = peewee.CharField(max_length=15)
    email = peewee.CharField(max_length=320)
    status = peewee.CharField(max_length=10) # "inACTIVE" or "active"
    creditlimit = peewee.CharField()


def add_customer(customer_ID, Name, Last_name, home_address, phone_number, email_address, status, credit_limit):
    try:
        with database.transaction():
            Customer.create(
                customer_id = customer_id,
                name = name,
                Last_name = Last_name,
                home_address = home_address,
                phone_number = phone_number,
                email = email,
                status = status,
                credit_limit = credit_limit
            )
            customer.save()
    except Exception as e:
        print(f"error creating {customer_id}")
        print(e)

def search_customers(customer_id):
    try:
        customer = Customer.get(customer.customer_id == customer_id)
        return {
            "name": customer.name,
            "last_name": customer.last_name,
            "phone_number": customer.phone_number,
            "email_address": customer.email,
        }
    except Exception as e:
        print(f"error reading customer {customer_id}")
        return{}


def delete_customer(customer_id):
    try:
        with database.transaction():
            customer = Customer.get(Customer.customer_id == customer_id)
            customer.delete_instance()
            customer.save()
            return True
    except Exception as e:
        print("Failed to delete")
        print(e)
        return False


def update_customer_credit(customer_id, new_credit_limit):
    try:
        with database.transaction():
            customer_credit_update = Customer.get_by_id(customer_id)
            customer_credit_update.credit_limit = new_credit_limit
            customer_credit_update.save()
    except Exception as e:
        print("Customer credit limit has updated")
        print(e)

def _list_active_customers():
    try:
        with database.transaction():
            customer_active = Customer.select().where(Customer.status == 'Active')
    except Exception as e:
            print('{} Active Customers'.format(len(customer_active)))
            return len(customer_active)

Customer.create_table()