from jospehring.domain.person import Person


def test_person_init_with_parameter():
    person = Person(name='david', number=5)

    assert person.name == 'david'
    assert person.num == 5


def test_person_init_without_parameter():
    person = Person()

    assert person.name is None
    assert person.num == 0


def test_person_the_value_of_age_less_than_zero():
    someone = Person(number=-3)

    assert someone.name is None
    assert someone.num == 0

