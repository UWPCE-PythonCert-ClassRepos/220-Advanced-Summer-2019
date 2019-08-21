import peewee

database = peewee.SqliteDatabase("customers.db")
database.connect()
database.execute_sql("drop table if exists customer;")

class BaseModel(peewee.Model):
    class Meta:
        database = database

class Customer(BaseModel):
    """
    This class defines Customer, which maintains details of someone

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
    lastname = peewee.CharField(max_length=50, null=True)
    address = peewee.CharField(max_length=75)
    phone_number = peewee.CharField(max_length=15)
    email = peewee.CharField(max_length=320)
    status = peewee.CharField(max_length=10)
    credit_limit = peewee.FloatField()

def create_customer_table():
    Customer.create_table()

def add_customer(customer_id, name, lastname, address, phone_number, email, status, credit_limit):
    try:
        if type(customer_id) != int:
            raise TypeError("Customer ID must be an Int")
        with database.transaction():
            customer = Customer.create(
                customer_id=customer_id,
                name=name,
                lastname=lastname,
                address=address,
                phone_number=phone_number,
                email=email,
                status=status.lower(),
                credit_limit=int(credit_limit),
            )
            customer.save()
            print("Database add successful")

    except Exception as e:
        print(f"error creating {customer_id}")
        print(e)
        print("See how the database protext our data")



def search_customer(customer_id):
    try:
        customer = Customer.get(Customer.customer_id == customer_id)
        return {
            "name": customer.name,
            "lastname": customer.lastname,
            "phone_number": customer.phone_number,
            "email": customer.email,
               }
    except Exception as e:
        print(f"error reading customer {customer_id}")
        print(e)
        return {}


def delete_customer(customer_id):
    try:
        customer = Customer.get(Customer.customer_id == customer_id)
        with database.transaction():
            Customer.delete_by_id(customer)
            customer.save()
            return True
    except Exception as e:
        print(f"error reading customer {customer_id}")
        print(e)
        return False

def update_customer_credit(customer_id, credit_limit):
    try:
        customer = Customer.get(Customer.customer_id == customer_id)
        # ques_update = float(input(" Please enter updated credit limit:  "))
        with database.transaction():
            customer.credit_limit = credit_limit
        customer.save()
    except Customer.DoesNotExist:
        raise ValueError("customer does not exist")
        print("transaction failed while updating cutomer ({customer_id}) credit limit")
        

def list_active_customers():
    try:
        return Customer.select().where(Customer.status == "active").count()
    except Exception as e:
        print(e)



if __name__ == "__main__":
    create_customer_table()
    add_customer(1, "john", "doe", "1234 main", "2061111111", "boya@gmail.com", "active", 500)
    add_customer(2, "jann", "doe", "1234 main", "2061111111", "girl@gmail.com", "Active", 1000)
    add_customer(3, "goober", "doe", "1234 main", "2061111113", "goobs@gmail.com", "active", 7000)
    delete_customer(1)
    print(search_customer(3))
    update_customer_credit(2, 10000)
    print(list_active_customers())


