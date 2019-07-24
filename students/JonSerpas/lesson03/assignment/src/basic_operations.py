import peewee


database = peewee.SqliteDatabase("customers.db")
try:
    database.connect()
except Exception as e:
    print(e)
database.execute_sql('PRAGMA foreign_keys = ON;')  # <-- can use this to execute sql cmds
# database.execute_sql('drop table if exists customer;')
# database.execute_sql('create table if NOT exists customer;')
# database.create_tables([customers])


class BaseModel(peewee.Model):
    class Meta:
        database = database

class Customer(BaseModel):
    '''
        Let's make some cusomters.
            Customer ID.
            Name.
            Lastname.
            Home address.
            Phone number.
            Email address.
            Status (active or inactive customer).
            Credit limit.
    '''

    customer_id = peewee.CharField(primary_key = True, max_length = 30)
    name = peewee.CharField(max_length=50)
    lastname = peewee.CharField(max_length=50, null=False)
    address = peewee.CharField(max_length=75)
    phone_number = peewee.CharField(max_length=15)
    email = peewee.CharField(max_length=320)  # based on max email add len search
    status = peewee.CharField(max_length=10) # inactive vs active
    credit_limit = peewee.FloatField()


def add_customer(customer_id, name, lastname, address,
                phone_number, email, status, credit_limit):
    try:
        with database.transaction():
            Customer.create(
                customer_id=customer_id,
                name=name,
                lastname=lastname,
                address=address,
                phone_number=phone_number,
                email=email,
                status=status,
                credit_limit=credit_limit
            )
    except Exception as e:
        print('error creating {customer_id}')
        print(e)

    Customer.save()

def search_customer(customer_id):
    # need to add error handling for not found. possibly with if statment
    try:
        customer = Customer.get(Customer.customer_id == customer_id)
        return {
            "name": customer.name,
            "name": customer.lastname,
            "name": customer.phone_number,
            "name": customer.email,
        }
    except Exception as e:
        print(e)

def show_all_customers():
    try:
        for customer in Customer:
            print(customer.customer_id, customer.email, customer.status)
    except Exception as e:
        print(e)

def delete_customer(customer_id):
    try:
        # customer = Customer.select().where(Customer.customer_id == customer_id)
        customer = Customer.get(Customer.customer_id == customer_id)
        customer.delete_instance()
        customer.save()
    except Exception as e:
        print(e)


def update_customer_credit(customer_id, new_credit_limit):
    try:
        with database.transaction():
           customer = Customer.get(Customer.customer_id == customer_id)
           customer.update(Customer.credit_limit == new_credit_limit)
           customer.save()
    except Exception as e:
        print(e)

def list_active_customers():
    # customer.select().where()
    try:
        #is_active = Customer.select().where(Customer.status == 'active')
        query = Customer.select().where(Customer.status == 'active')
        for active_customer in query:
            print(active_customer.customer_id, active_customer.name, active_customer.status)
    except ValueError:
        print('Customer not found.')


database.create_tables([Customer])

