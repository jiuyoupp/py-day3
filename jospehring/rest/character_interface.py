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
        print(cls.jospeh.next())

    @classmethod
    def show_jospeh(cls):
        print(cls.jospeh.query_list)


class CharacterInterface(Interface):
    def execute(self):
        while True:
            for index, item in enumerate(self.option_list, 1):
                print(index, item[0])
            choice = input('请输入您选择的序号').strip()
            if choice.isdecimal() and 1 <= int(choice) <= len(self.option_list):
                choice = int(choice)
                if hasattr(type(self), self.option_list[choice-1][1]) and callable(getattr(type(self), self.option_list[choice-1][1])):
                    ret = getattr(type(self), self.option_list[choice-1][1])()
                    if ret:
                        return ret
                else:
                    print('方法未定义或不可调用')
            else:
                print('您输入的序号y有误，请检查后重新输入！')


class QtInterface(Interface):
    def execute(self):
        pass


def run(Interface):
    while True:
        obj = Interface()
        ret = obj.execute()
        if ret == 'exit':
            break

if __name__ == '__main__':
    run(CharacterInterface)