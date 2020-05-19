from jospehring.usecase.interface import Interface
from jospehring.domain.ring import Ring
from jospehring.usecase.reader_use_case import read_data
from PySide2.QtWidgets import QApplication, QWidget, QDialog
from jospehring.rest.ui_main import Ui_Form
from jospehring.rest.child import Ui_Dialog
import sys


class MyMainWindow(QWidget, Ui_Form, Interface):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.pushButton.clicked.connect(lambda: self.execute('1'))
        self.pushButton_2.clicked.connect(lambda: self.execute('2'))
        self.pushButton_3.clicked.connect(lambda: self.execute('3'))
        self.pushButton_4.clicked.connect(lambda: self.execute('4'))
        self.pushButton_5.clicked.connect(lambda: self.execute('5'))
        self.pushButton_6.clicked.connect(lambda: self.execute('6'))

    def next_people(self):
        outperson = self.jospeh.next()
        c = outperson.name + str(outperson.num)
        self.textEdit.setPlainText (c)

    def exit(self):
        print('退出本程序！')
        sys.exit(0)

    def reset(self):

        dialog = ChildWindow(self)
        dialog.comboBox.clear()
        dialog.exec_()
        step, location = dialog.reset_data()
        step = int(step)
        location = int(location)
        dialog.destroy()
        self.jospeh.reset(step, location)

    def show_menu(self):
        for index, item in enumerate(self.option_list, 1):
            print(index, item[0])

    def create_jospehring(self, obj=Ring, start=0, location=0):
        self.jospeh = obj()
        if self.jospeh:
            dialog = ChildWindow(self)
            dialog.exec_()
            step, location, path = dialog.get_data()
            step = int(step)
            location = int(location)
            dialog.destroy()
            reader = read_data(path, 'r')
            self.jospeh.from_reader(reader)
            self.jospeh.reset(step, location)

    def next_people(self):
        outperson = self.jospeh.next()
        self.textEdit.setPlainText(outperson.name+str(outperson.num))

    def show_jospeh(self):
        ring = self.jospeh.query_list()
        outdata = ''
        for person in ring:
            outdata += person.name + str(person.num) + '\n'
        self.textEdit.setPlainText(outdata)

    def out_sequnece(self):
        jospehring = self.jospeh.popelem()
        outdata = ''
        for person in jospehring:
            outdata += person.name + str(person.num) + '\n'
        self.textEdit.setPlainText(outdata)

    def execute(self, choice):
        if 1 <= int(choice) <= len(self.option_list):
            choice = int(choice)
            temp = callable(getattr(type(self), self.option_list[choice - 1][1]))
            if hasattr(type(self), self.option_list[choice - 1][1]) and temp is True:
                # 反射不能使用self. 的形式，将self进行传参
                ret = getattr(type(self), self.option_list[choice - 1][1])(self)
                if ret:
                    return ret
            else:
                print('方法未定义或不可调用')
        else:
            print('您输入的序号y有误，请检查后重新输入！')


class ChildWindow(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(ChildWindow, self).__init__(parent)
        self.setupUi(self)

    def get_data(self):
        text1 = self.lineEdit.text()
        text2 = self.lineEdit_2.text()
        path = self.comboBox.currentText()
        return text1, text2, path

    def reset_data(self):
        text1 = self.lineEdit.text()
        text2 = self.lineEdit_2.text()
        return text1, text2
if __name__ == '__main__':

    app = QApplication(sys.argv)
    obj = MyMainWindow()
    obj.show()
    sys.exit(app.exec_())