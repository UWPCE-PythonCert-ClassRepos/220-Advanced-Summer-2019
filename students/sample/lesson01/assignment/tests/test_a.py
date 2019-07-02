"""

I am test_a.py in students/yourname/lessons/lesson99/assignments/tests
run me from  students/yourname/lessons/lesson99/assignments/src


Linting:
pytest --pylint

Test and coverage:
python -m pytest -vv --cov=.  ../tests/


Note my import conventions. Verbose maybe, but it makes it
COMPLETELY CLEAR where the imported funcitonlaity comes from

"""

import pytest
import a
import b
import c


def test_a():
    a.main()
    assert 1 == 1

def test_b():
    b.print_mess("B")
    assert 2 == 2

def test_c():
    c.show_mess("C")
    assert 3 == 3