import peewee
import logging
log_format = "%(asctime)s %(filename)s:%(lineno)-3d %(levelname)s %(message)s"
logging.basicConfig(level=logging.INFO, format=log_format, filename='db.log')

database = peewee.SqliteDatabase("customers.db")


try:
    database.connect()
    logging.info('Database connected')
except Exception as e:
    print(e)
    logging.warning('Database connection failed!')

# -- can use this to execute sql cmds--
database.execute_sql('PRAGMA foreign_keys = ON;')
database.execute_sql('DROP TABLE customer')


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
            customer = Customer.create(
                customer_id=customer_id,
                name=name,
                lastname=lastname,
                address=address,
                phone_number=phone_number,
                email=email,
                status=status,
                credit_limit=credit_limit
            )
            customer.save()
            print('successfully added customer')
            logging.info(f'customer {customer_id} added to database')
    except TypeError:
        logging.info(f'stupid typeerror - should troubleshoot')
        pass
    except Exception as e:
        print(f'error creating {customer_id}')
        print(e)
        logging.error(f'error creating {customer_id} {name} in database')
        

    


def search_customer(customer_id):
    # need to add error handling for not found. possibly with if statment
    try:
        customer = Customer.get(Customer.customer_id == customer_id)
        return {
            "name": customer.name,
            "lastname": customer.lastname,
            "phone_number": customer.phone_number,
            "email": customer.email,
            "credit limit": customer.credit_limit
        }
        logging.info(f'search completed for customer {customer_id}')
    except Exception as e:
        print(f"error retreiving {customer_id}")
        logging.error(f'error retreiving {customer_id} from database')
        print(e)
        return {}

def show_all_customers():
    try:
        for customer in Customer:
            print(customer.customer_id, customer.email, customer.status)
        logging.info(f'showing all customers from db')
    except Exception as e:
        logging.error('unable to search database')
        print(e)

def delete_customer(customer_id):
    try:
        # customer = Customer.select().where(Customer.customer_id == customer_id)
        with database.transaction():
            try:
                customer = Customer.get(Customer.customer_id == customer_id)
                customer.delete_instance()
                customer.save()
                return True
                logging.info(f'deleted {customer_id}, {name} from database lol')
            except Exception as e:
                print(e)
                pass
    except Exception as e:
        print('failed deleting customer')
        logging.error(f'failed deleting {customer_id}, {name}')
        print(e)
        return False


def update_customer_credit(customer_id, new_credit_limit):
    try:
        with database.transaction():
            customer = Customer.get(Customer.customer_id == customer_id)
            print(customer)
            # customer.credit_limit = credit_limit <-- try this later instead of update
            customer.update(Customer.credit_limit == new_credit_limit)
            customer.save()
            logging.info(f'customer {customer_id} credit updated from {Customer.credit_limit} to {new_credit_limit}')
    except Customer.DoesNotExist as dne:
        return dne
    except Exception as e:
        logging.error(f'unable to update {customer_id}')
        print(e)

def list_active_customers():
    try:
        #is_active = Customer.select().where(Customer.status == 'active')
        query = Customer.select().where(Customer.status == 'active')
        for active_customer in query:
            # print(active_customer.customer_id, active_customer.name, active_customer.status)
            print(f"{active_customer.name} {active_customer.lastname}'s status is {active_customer.status}")
    except ValueError:
        print('No active customers found.')
        logging.error(f'failed to list active customers')

    return(query)

def toggle_status(customer_id):
    try:
        with database.transaction():
            customer = Customer.get(Customer.customer_id == customer_id)
    except Exception as e:
        print(e)

    print(customer.name, customer.status)
    set_status = input(f'Enter new status for {customer.name}- (active / inactive / none: )').lower()
    if set_status == 'active':
        customer.update(Customer.status == "active")
        logging.info(f'customer {customer_id} set to active')
    elif set_status == 'inactive':
        customer.update(Customer.status == "inactive")
        logging.info(f'customer {customer_id} set to inactive')
    else:
        pass
    customer.save()

    return{
            "name": customer.name,
            "status": customer.status
        }


database.create_tables([Customer])

if __name__ == "__main__":
    data = []
    logging.info(f'initializing....')

