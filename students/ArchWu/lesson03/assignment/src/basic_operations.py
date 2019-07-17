import peewee

database = peewee.SqliteDatabase("customers.db")
database.connect()
database.execute_sql('drop table if exists customer;')

class BaseModel(Model):
    class Meta:
        database = database

class Customer(BaseModel):
    customer_id = CharField(primary_key=True, max_length=30)
    name = peewee.CharField(max_length=50)
    lastname = peewee.CharField(max_length=50, null=False)
    address = peewee.CharField(max_length=75)
    phone_number = peewee.CharField(max_length=15)
    email = peewee.CharField(max_length=320)
    status = peewee.CharField(max_length=10)
    credit_limit = peewee.FloatField()

def add_customer(customer_id, name, lastname, address, phone_number, email, status, credit_limit):
    try:
        with database.transaction():
            customer.create(
                customer_id = customer_id
                name = name
                lastname = lastname
                address = address
                phone_number = phone_number
                email = email
                status = status
                credit_limit = credit_limit
            )
            customer.save()

    except Exception as e:
        print(e)

def search_customer(customer_id):
    try:
        customer = Customer.get()
