"""
basic operations module
"""
import peewee
import logging

database = peewee.SqliteDatabase("customer.db")
database.connect()
database.execute_sql('drop table if exists customer;')
database.execute_sql("PRAGMA foreign_keys=ON;")

log_format = "%(asctime)s %(filename)s:%(lineno)-3d %(levelname)s %(message)s"
log_file = "db.log"

formatter = logging.Formatter(log_format)
file_handler = logging.FileHandler(log_file)
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.INFO)
logger = logging.getLogger()
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


class BaseModel(peewee.Model):
    """
    Base model for database
    """
    class Meta:
        """
        database
        """
        database = database


class Customer(BaseModel):
    """
    Class defines Customer as stores their information
    """
    customer_id = peewee.CharField(primary_key=True, max_length=50)
    name = peewee.CharField(max_length=20)
    lastname = peewee.CharField(max_length=20, null=True)
    home_address = peewee.CharField(max_length=50)
    phone_number = peewee.CharField(max_length=30)
    email_address = peewee.CharField(max_length=100)
    status = peewee.CharField(max_length=10)
    credit_limit = peewee.FloatField()


def add_customer(customer_id, name, lastname, home_address,
                 phone_number, email_address, status, credit_limit):
    """
    This function will add a new customer to the sqlite3 database
    """
    try:
        with database.transaction():
            customer = Customer.create(
                customer_id=customer_id,
                name=name,
                lastname=lastname,
                home_address=home_address,
                phone_number=phone_number,
                email_address=email_address,
                status=status,
                credit_limit=credit_limit,
            )
            logger.info(
                f"Successfully added customer {customer_id} with {credit_limit}"
            )
            customer.save()
    except Exception as unknown_error:
        logger.error(
            f"Error. Failed to added customer {customer_id}. {unknown_error}"
        )
        print(unknown_error)


def search_customer(customer_id):
    """
    This function will return a dictionary object with name,
    lastname, email address and phone number of a customer or
    an empty dictionary object if no customer was found
    """
    try:
        customer = Customer.get(Customer.customer_id == customer_id)
        logger.info(f"Successfully found customer {customer_id}")
        return {
            'name': customer.name,
            'lastname': customer.lastname,
            'email_address': customer.email_address,
            'phone_number': customer.phone_number
        }
    except Exception as unknown_error:
        logger.error(
            f"Error. Failed to find customer {customer_id}. {unknown_error}"
        )
        print(f"Error. Could not find customer {customer_id}. {unknown_error}")
        return {}


def delete_customer(customer_id):
    """
    This function will delete a customer from the sqlite3 database.
    """
    try:
        with database.transaction():
            customer = Customer.get(Customer.customer_id == customer_id)
            customer.delete_instance()
            customer.save()
            logger.info(f"Successfully deleted customer {customer_id}")
    except Exception as unknown_error:
        logger.error(
            f"Error. Failed to delete customer {customer_id}. {unknown_error}"
        )
        print(
            f'Error. Could not delete customer {customer_id}. {unknown_error}'
        )


def update_customer_credit(customer_id, credit_limit):
    """
    This function will search an existing customer by
    customer_id and update their credit limit or raise a
    ValueError exception if the customer does not exist.
    """
    try:
        with database.transaction():
            customer = Customer.get_by_id(customer_id)
            customer.credit_limit = credit_limit
            customer.save()
            logger.info(
                f"Successfully updated customer {customer_id} credit limit"
            )
    except Exception as unknown_error:
        logger.error(
            f"Error. Failed to update customer {customer_id}"
            " credit limit. {unknown_error}"
        )
        print(f'Error. Cutomer {customer_id} does not exist. {unknown_error}')
        raise ValueError


def list_active_customers():
    """
    This function will return an integer with the
    number of customers whose status is currently active.
    """
    try:
        active_customer_count = 0
        for _ in Customer.select().where(Customer.status == 'Active'):
            active_customer_count += 1
        logger.info(
            f"Successfully counted active customers {active_customer_count}"
        )
        return active_customer_count
    except Exception as unknown_error:
        logger.error(f"Error. Failed to count customers. {unknown_error}")
        print(
            f'Error. Not able to count number of active customers.'
            ' {unknown_error}'
        )


def make_generators_from_csv(csv_file):
    """
    Make generator from csv file where it
    yields lists of inputs for adding customers
    """
    with open(csv_file, mode='r', encoding='utf-8',
              errors='ignore') as source_data:
        source_data.readline()  # skip header

        for line in source_data.readlines():
            try:
                line = line.rstrip().split(',')
                if len(line) == 8:
                    yield line
                else:
                    logger.error(
                        f"Import failure on line split."
                        " Expected 8 columns, but got {len(line)}. {line}"
                    )
            except IndexError as e:
                logger.error(f"Could not import customer data for {line}: {e}")


if __name__ == "__main__":
    Customer.create_table()
    message_starting = "Starting with creating generator from DB import"
    logger.info(message_starting)
    print(message_starting)
    customer_generator = make_generators_from_csv("customer.csv")
    message_generator = "Generators Complete, Starting to add customers"
    logger.info(message_generator)
    print(message_generator)
    [add_customer(*line) for line in customer_generator]  # Painfully slow
    message_done = "DB import complete"
    logger.info(message_done)
    print(message_done)
