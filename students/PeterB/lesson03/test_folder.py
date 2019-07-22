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


def add_customer(Customer ID, Name, Lastname, Home address, Phone number, Email address, Status (active or inactive customer), Credit limit):
    try:
        with database.transaction():
            Customer.create(
                customer_id=customer_id,
                name=name,
                lastname=lastname,
                address=address,
                phonenumber=phonenumber,
                email=email,
                status=status
                creditlimit=creditlimit
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
            "lastname": customer.lastname,
            "phonenumber": customer.phonenumber,
            "email": customer.email,
        }
    except Exception as e:
        print(f"error reading customer {customer_id}")
        return{}


def delete_customer(customer_id):
    try:
        with database.transaction():
            pass
    except Exception as e:
        print(e)

def update_customer_credit(customer_id, credit_limit)
    try:
        with database.transaction():
            pass
    except Exception as e:
        print(e)

def _list_active_customers():param*args
    customer.select().where()
