import peewee
import logging

database = peewee.SqliteDatabase("customers.db")
database.connect()
database.execute_sql('PRAGMA foreign_key = ON;')
database.execute_sql('drop table if exists customer;')


class BaseModel(peewee.Model):
    class Meta:
        database = database


class Customer(BaseModel):
    """
    This class defines a Customer in the databaase
        Customer ID.
        Name.
        Lastname.
        Home address.
        Phone number.
        Email address.
        Status (active or inactive customer).
        Credit limit.
    """
    customer_id = peewee.CharField(primary_key=True, max_length=30)
    name = peewee.CharField(max_length=50)
    last_name = peewee.CharField(max_length=50, null=True)
    address = peewee.CharField(max_length=75)
    phone_number = peewee.CharField(max_length=15)
    email = peewee.CharField(max_length=320) # based on max email address length search
    status = peewee.CharField(max_length=10) # "Inactive" or "Active"
    credit_limit = peewee.FloatField()


def create_tables():
    with database.transaction():
        database.create_tables([Customer])

def drop_tables():
    with database.transaction():
        database.drop_tables([Customer])

def add_customer(customer_id, name, last_name, address, phone_number, email, status, credit_limit):
    try:
        with database.transaction():
            customer = Customer.create(
                customer_id=customer_id,
                name=name,
                last_name=last_name,
                address=address,
                phone_number=phone_number,
                email=email,
                status=status,
                credit_limit=credit_limit
            )
            print(f"Customer saved {name}")

    except Exception as e:
        logging.warning(f"error creating {customer_id}")
        logging.warning(e)


def search_customer(customer_id):
    try:
        customer = Customer.get(Customer.customer_id == customer_id)
        return {
            "name": customer.name,
            "last_name": customer.last_name,
            "phone_number": customer.phone_number,
            "email": customer.email,
        }
    except Exception as e:
        logging.warning(f"error reading customer {customer_id}")
        logging.warning(e)
        return {}


def delete_customer(customer_id):
    try:
        customer = Customer.get(Customer.customer_id == customer_id)
        with database.transaction():
            customer.delete_instance()
            return True
    except Exception as e:
        logging.warning(e)
        return False


def update_customer_credit(customer_id, credit_limit):
    try:
        with database.transaction():
            customer = Customer.get(Customer.customer_id == customer_id)
            customer.credit_limit = credit_limit
            customer.save()
    except Exception as e:
        raise ValueError("NoCustomer {}".format(customer_id))


def list_active_customers():
    try:
        active_customers = Customer.select().where(Customer.status == 'active')
        for customer in active_customers:
            print(f"{customer.name} {customer.last_name} status is {customer.status}")
        return len(active_customers)
    except Exception as e:
        print(e)
        return 0


if __name__ == '__main__':
    add_customer(1, "Sally", "Shen", "5859 20th pl., Seattle, WA, 98115", "917-888-9999",
                 "shenyingyy@gmail.com", "active", 2000)

if __name__ == '__main__':
    data = []
    (add_customer(c) for c in data)
