# They are not, in fact, constants...
# pylint: disable=C0103
# Seems to be a pylint false positive?
# pylint: disable=E1120
"""
basic_operations.py

peewee
# model = table
# field instance = column
# model instance = row
"""

import peewee

customer_db = peewee.SqliteDatabase("customers.db")


class BaseModel(peewee.Model):
    """peewee basemodel"""
    class Meta:
        """Inner class"""
        # database is a keyword and must be set
        database = customer_db


class Customer(BaseModel):
    """Defines the Customer model (table)"""
    customer_id = peewee.CharField(primary_key=True, max_length=30)
    name = peewee.CharField(max_length=50)
    lastname = peewee.CharField(max_length=50, null=True)
    homeaddress = peewee.CharField(max_length=75)
    phone_number = peewee.CharField(max_length=15)
    email = peewee.CharField(max_length=320)
    status = peewee.CharField(max_length=15)
    credit_limit = peewee.FloatField()


customer_db.connect()
customer_db.execute_sql('drop table if exists customer;')
customer_db.create_tables([Customer])


def add_customer(customer_id, name, lastname, homeaddress, phone_number, email, status, credit_limit):
    """Adds customer to DB"""
    try:
        with customer_db.transaction():

            Customer.insert(
                customer_id=customer_id,
                name=name,
                lastname=lastname,
                homeaddress=homeaddress,
                phone_number=phone_number,
                email=email,
                status=status,
                credit_limit=credit_limit
            ).execute()
    # Unfortunately the peewee documentation isn't very good about documenting it's exceptions :(
    except Exception as e:  # pylint: disable=W0703
        print("Error creating customer_id {}: {}".format(customer_id, e))


def delete_customer(customer_id):
    """Deletes customer from DB"""
    try:
        with customer_db.transaction():
            result = Customer.delete().where(Customer.customer_id == customer_id).execute()
            if result == 1:
                return True
            return False
    # Unfortunately the peewee documentation isn't very good about documenting it's exceptions :(
    except Exception as e:  # pylint: disable=W0703
        print("Error deleting {}: {}".format(customer_id, e))


def list_active_customers():
    """Lists active customers"""
    try:
        with customer_db.transaction():
            active_customers = []
            # Pylint false positive, Customer.select() definitely returns something ;)
            query = Customer.select().where(Customer.status == 'active')  # pylint: disable=E1111
            for customer in query:
                active_customers.append(customer)
            return len(active_customers)
    # Unfortunately the peewee documentation isn't very good about documenting it's exceptions :(
    except Exception as e:  # pylint: disable=W0703
        print("Error listing active customers: {}".format(e))


def search_customer(customer_id):
    """Searches DB for customer_id"""
    try:
        with customer_db.transaction():
            search_result = Customer.select().where(Customer.customer_id == customer_id).get()
            if search_result:
                return {
                    "name": search_result.name,
                    "lastname": search_result.lastname,
                    "phone_number": search_result.phone_number,
                    "email": search_result.email,
                    "status": search_result.status,
                    "credit_limit": search_result.credit_limit
                }
            return {}
    except Customer.DoesNotExist as e:
        print("Error retrieving {}: {}".format(customer_id, e))
        return {}


def update_customer_credit(customer_id, credit_limit):
    """Updates the credit_limit of customer_id"""
    try:
        with customer_db.transaction():
            customer = Customer.select().where(Customer.customer_id == customer_id).get()
            customer.credit_limit = credit_limit
            customer.save()

    except Customer.DoesNotExist as e:
        print("Error updating credit limit for customer {}: {}".format(customer_id, e))
        # Absolutely could not get pylint to recognize peewee's DoesNotExist error type, so raise ValueError instead
        raise ValueError("NoCustomer")


if __name__ == '__main__':
    with open('customer.csv', 'r', encoding='iso-8859-15') as input_file:
        for line in input_file:
            values = line.split(",")
            if 'Id' not in values[0]:
                add_customer(*values)
    print(Customer.select().count())
