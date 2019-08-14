



import pytest
import basic_operations as b_ops


@pytest.fixture
def _add_customers():
    """
    possible refactor could be defining the dict as a constant then calling each key in the specific method.
    see chapter 2 from above book:
Without Setup
class TestCalculate(unittest.TestCase):
    def test_add_method_returns_correct_result(self):
      calc = Calculate()
        self.assertEqual(4, calc.add(2,2))
    def test_add_method_raises_typeerror_if_not_ints(self):
        calc = Calculate()
        self.assertRaises(TypeError, calc.add, "Hello", "World")
if __name__ == '__main__':
    unittest.main()
With Setup
class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculate()
    def test_add_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.add(2,2))
    def test_add_method_raises_typeerror_if_not_ints(self):
        self.assertRaises(TypeError, self.calc.add, "Hello", "World")
    :return:
    """
    customer_dict = {'customer_id': '6', 'first_name': 'Katee', 'last_name': 'Jane',
                     'home_address': 'lkasdjf', 'phone_number': '9876',
                     'email_address': 'none', 'customer_status': 'A',
                     'credit_limit': '231'}
    return customer_dict


@pytest.fixture
def _search_customers():
    customer_id = 6
    return customer_id


@pytest.fixture
def _delete_customers():
    customer_id = 6
    return customer_id


@pytest.fixture
def _update_customer_credit():
    customer_id = 6
    new_credit = 369
    return customer_id, new_credit


@pytest.fixture
def _list_active_customers():
    return []


def test_list_active_customers(_list_active_customers):
    """ actives """

    actives = b_ops.list_active_customers()

    assert actives == 2


def test_add_customer(_add_customers):
    """ additions
    """

    b_ops.add_customer(_add_customers)
    added = b_ops.search_customer(6)
    assert added["first_name"] == 'Katee'
    assert added["last_name"] == 'Jane'
    assert added["email_address"] == 'none'
    assert added["phone_number"] == 9876
    b_ops.delete_customer(6)


def test_search_customer(_search_customers):
    """ search """
    result = b_ops.search_customer(_search_customers)
    assert result == {'customer_id': '6', 'first_name': 'Katee', 'last_name': 'Jane',
                      'home_address': 'lkasdjf', 'phone_number': '9876',
                      'email_address': 'none', 'customer_status': 'A',
                      'credit_limit': '231'}

    result = b_ops.search_customer(_search_customers)
    assert result["name"] == 'Katee'
    assert result["lastname"] == 'Jane'


def test_update_customer_credit(_update_customer_credit):
    """ update """
    b_ops.update_customer_credit(_update_customer_credit)
    with pytest.raises(ValueError) as excinfo:
        b_ops.update_customer_credit("00100", 1000)  # error
        assert 'NoCustomer' in str(excinfo.value)


def test_delete_customer(_delete_customers):
    """ delete """

    response = b_ops.delete_customer(_delete_customers)
    assert response is True

    deleted = b_ops.search_customer(_delete_customers)
    assert deleted == {}
