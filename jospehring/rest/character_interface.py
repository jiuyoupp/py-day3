from jospehring.usecase.interface import Interface


class CharacterInterface(Interface):
    def execute(self):
        while True:
            for index, item in enumerate(self.option_list, 1):
                print(index, item[0])
            choice = input('请输入您选择的序号').strip()
            if choice.isdecimal() and 1 <= int(choice) <= len(self.option_list):
                choice = int(choice)
                # 使用type防止得到实例的属性及方法
                temp = callable(getattr(type(self), self.option_list[choice - 1][1]))
                if hasattr(type(self), self.option_list[choice-1][1]) and temp is True:
                    ret = getattr(type(self), self.option_list[choice-1][1])()
                else:
                    print('方法未定义或不可调用')
            else:
                print('您输入的序号y有误，请检查后重新输入！')


def run(interface: Interface) -> None:
    while True:
        obj = interface()
        ret = obj.execute()
        if ret == 'exit':
            break

