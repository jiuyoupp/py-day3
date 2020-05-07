import pytest
from homework_joseph import Person


def test_person_init():
    person = Person(name='david', number=5)

    assert person.name == 'david'
    assert person.num == 5


if __name__ == '__main__':
    pytest.main(['test_person.py'])