from jospehring.domain.person import Person
from jospehring.usecase.ring import Ring


def test_ring_init():
    jospeh = Ring()
    assert jospeh.start == 0
    assert jospeh.step == 1
    assert jospeh._ring ==[]
    assert jospeh._temp == []
    assert jospeh._current_id == 0


def test_ring_reset():
    jospeh = Ring()
    jospeh.reset(step=1, location=2)
    assert jospeh.step == 1
    assert jospeh.start+1 == 2


def test_ring_pop():
    jospeh = Ring()
    person1 = Person(name='jack', number=13)
    jospeh.append(person1)
    outelem = jospeh.pop(0)
    assert person1 == outelem


def test_josephus_append():
    jos = Ring()
    person = Person('Bob', 12)
    jos.append(person)
    assert jos._ring == [person]


def test_ring_query():
    jospeh = Ring()
    peron1 = Person(name='jack', number=13)
    peron2 = Person(name='lili', number=18)
    people = [peron1, peron2]
    jospeh.append(peron1)
    jospeh.append(peron2)
    assert jospeh.query_list() == people


def test_ring_popelem():
    jospeh = Ring()
    person1 = Person(name='jack', number=13)
    person2 = Person(name='lili', number=18)
    person3 = Person(name='david', number=20)
    personlist = [person1, person2, person3]

    for person in personlist:
        jospeh.append(person)
    jospeh.reset(step=1, location=1)  # start = location-1
    # temp采用了拷贝得到的perosn实例与原来不同
    outperson1 = next(jospeh)
    outperson2 = next(jospeh)
    outperson3 = next(jospeh)

    assert outperson1.name == person1.name
    assert outperson1.num == person1.num
    assert outperson2.name == person2.name
    assert outperson2.num == person2.num
    assert outperson3.name == person3.name
    assert outperson3.num == person3.num


def test_is_empty():
    jos = Ring()
    judgeempty = jos.is_empty()
    assert judgeempty is True


def test_from_reader():
    person1 = Person(name='jack', number=13)
    person2 = Person(name='lili', number=18)
    person3 = Person(name='david', number=20)
    people = [person1, person2, person3]
    jospeh = Ring()
    jospeh.from_reader(people)
    assert jospeh._ring == people



