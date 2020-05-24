from jospehring.usecase.ring import Ring
from jospehring.adapter.reader import read_data


class Interface(object):
    option_list = [
        ('create a josephring', 'create_jospehring'), ('the next kill', 'next_people'),
        ('output sequence', 'out_sequnece'), ('reset the start and location', 'reset'),
        ('show joseph', 'show_jospeh'), ('exit the programme', 'exit')
    ]
    jospeh = None

    def execute(self, choice = 0):
        raise NotImplementedError('没有执行界面')

    def exit(self):
        print('退出本程序！')
        return 'exit'

    def reset(self):
        step = input('请输入start')
        location = input('请输入location')
        if step.isdecimal() is True and location.isdecimal() is True:
            step = int(step)
            location = int(location)
            self.jospeh.reset(step, location)
        else:
            print('输入的不是数字')

    def show_menu(self):
        for index, item in enumerate(self.option_list, 1):
            print(index, item[0])

    def create_jospehring(self, obj=Ring):
        self.jospeh = obj()
        path = input('输入文件的路径')
        try:
            reader = read_data(path, 'r')
        except FileNotFoundError as e:
            print('打不开要找的文件')
        else:
            self.jospeh.from_reader(reader)
            if not (self.jospeh is None):
                self.reset()

    def next_people(self):
        try:
            outperson = next(self.jospeh)
            print(outperson.name, outperson.num)
        except StopIteration as e:
            print('环为空')


    def show_jospeh(self):
        ring = self.jospeh.query_list()
        for person in ring:
            print(person.name, person.num)

    def out_sequnece(self):
        jospehring = self.jospeh
        if jospehring.is_empty():
            print('环为空')
        for person in jospehring:
            print(person.name, person.num)
