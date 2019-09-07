"""
"""

import pytest
import parallel

@pytest.fixture
def _all_answers():
    """
    underscore required on fixture to eliminate an
    invalid redefinition warning
    from pytest pylint

    """

    # answers_linear = linear.import_data('data', 'customers.csv', 'products.csv')
    answers_parallel = parallel.import_data('data', 'customers.csv', 'products.csv')

    return ({
        # "processed": answers_linear[0][0],
        # "count_prior": answers_linear[0][1],
        # "count_new": answers_linear[0][2],
        # "elapsed": answers_linear[0][3]
        # },
        # {
        # "processed": answers_linear[1][0],
        # "count_prior": answers_linear[1][1],
        # "count_new": answers_linear[1][2],
        # "elapsed": answers_linear[1][3]
        # },
        # {
        "processed": answers_parallel[0][0],
        "count_prior": answers_parallel[0][1],
        "count_new": answers_parallel[0][2],
        "elapsed": answers_parallel[0][3]
        },
        {
        "processed": answers_parallel[1][0],
        "count_prior": answers_parallel[1][1],
        "count_new": answers_parallel[1][2],
        "elapsed": answers_parallel[1][3]
        }
        )


def test_submission(_all_answers):
    #linear cust/prod, parallel cust/prod
    for answer in _all_answers:
        # needs a few more
        assert type(answer["processed"]) == int
        assert type(answer["count_prior"]) == int
        assert type(answer["count_new"]) == int
        assert answer["count_prior"] + answer["processed"] == answer["count_new"]
        assert type(answer["elapsed"]) == float
        assert answer["elapsed"] > 0.0


