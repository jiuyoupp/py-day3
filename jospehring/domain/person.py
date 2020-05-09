class Person(object):
    def __init__(self, name=None, number=None) -> None:
        self.name = name
        if number <= 0:
            raise ValueError('number must bigger than 0')
        self.num = number

