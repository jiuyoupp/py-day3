import pytest
from jospehring.domain.person import Person
from jospehring.adapter.reader import ZipReader
from jospehring.adapter.reader import TxtReader
from jospehring.adapter.reader import CsvReader


@pytest.fixture()
def zipfilepath():
    return r'D:\pythoncode\josphering\data\peopledata.zip'


@pytest.fixture()
def txtfilepath():
    return r'D:\pythoncode\josphering\data\peopledata.txt'


@pytest.fixture()
def csvfilepath():
    return r'D:\pythoncode\josphering\data\peopledata.csv'


@pytest.fixture()
def peopledata():
    return [
        Person('冯巧', 1), Person('昌瑶灵', 2), Person('袁春绿', 3),
        Person('吕天', 4), Person('金迎夜', 5), Person('潘海曼', 6),
        Person('尤文白', 7), Person('凤千谷', 8), Person('杨岚', 9),
        Person('陶晓', 10)
    ]


def test_zipreader(zipfilepath, peopledata):
    zipreader = ZipReader()
    reader = zipreader.reader(zipfilepath, 'r')
    people = []
    for i in reader:
        people.append(i)

    person1 = people[0]
    outperson1 = peopledata[0]
    person2 = people[1]
    outperson2 = peopledata[1]

    assert person1.name == outperson1.name
    assert person1.num == outperson1.num
    assert person2.name == outperson2.name
    assert person2.num == outperson2.num


def test_txtreader(txtfilepath, peopledata):
    txtreader = TxtReader()
    reader = txtreader.reader(txtfilepath, 'r')
    people = []
    for i in reader:
        people.append(i)

    person1 = people[0]
    outperson1 = peopledata[0]
    person2 = people[1]
    outperson2 = peopledata[1]

    assert person2.name == outperson2.name
    assert person2.num == outperson2.num
    assert person1.name == outperson1.name
    assert person1.num == outperson1.num


def csv_txtreader(csvfilepath, peopledata):
    csvreader = CsvReader()
    reader = csvreader.reader(csvfilepath, 'r')
    people = []
    for i in reader:
        people.append(i)

    person1 = people[0]
    outperson1 = peopledata[0]
    person2 = people[1]
    outperson2 = peopledata[1]

    assert person2.name == outperson2.name
    assert person2.num == outperson2.num
    assert person1.name == outperson1.name
    assert person1.num == outperson1.num

