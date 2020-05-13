from jospehring.domain.ring import Ring
from jospehring.usecase.reader_use_case import read_data
from jospehring.usecase.reader import ZipReader


class Interface(object):
    option_list = [
        ('create a josephring', 'create_jospehring'), ('the next kill', 'next_people'),
        ('output sequence', 'out_sequnece'), ('reset the start and location', 'reset'),
        ('show joseph', 'show_jospeh'), ('exit the programme', 'exit')
    ]
    jospeh = None

    @classmethod
    def execute(cls):
        raise NotImplementedError('没有执行界面')

    @classmethod
    def exit(cls):
        print('退出本程序！')
        return 'exit'

    @classmethod
    def reset(cls):
        step = int(input('请输入start'))
        location = int(input('请输入location'))
        cls.jospeh.reset(step, location)
    @classmethod
    def show_menu(cls):
        for index, item in enumerate(cls.option_list, 1):
            print(index, item[0])

    @classmethod
    def create_jospehring(cls, obj=Ring):
        cls.jospeh = obj()
        readdata = ZipReader()
        reader = read_data(readdata, 'D:\pythoncode\josphering\data\peopledata.zip', 'r')
        cls.jospeh.from_reader(reader)
        if cls.jospeh:
            start = int(input('please input start'))
            location = int(input('please input location'))
            cls.jospeh.reset(start, location)


    @classmethod
    def next_people(cls):
        outperson = cls.jospeh.next()
        print(outperson.name, outperson.num)

    @classmethod
    def show_jospeh(cls):
        ring = cls.jospeh.query_list()
        for person in ring:
            print(person.name, person.num)

    @classmethod
    def out_sequnece(cls):
        jospehring = cls.jospeh.popelem()
        for person in jospehring:
            print(person.name, person.num)