from jospehring.usecase.interface import Interface
from jospehring.domain.ring import Ring
from jospehring.usecase.reader_use_case import read_data
from jospehring.usecase.reader import ZipReader
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton,  QPlainTextEdit, QWidget,  QLineEdit, QDialog, QVBoxLayout, QTileRules,QDialogButtonBox
from PySide2 import QtCore
import sys


class QtInterface(QWidget, Interface):
    def __init__(self, parent=None):
        super(QtInterface, self).__init__(parent)
        self.resize(400, 90)
        self.setWindowTitle('对话框关闭时返回值给主窗口例子')

        self.textEdit = QPlainTextEdit(self)
        self.textEdit.setPlaceholderText("请选择序号进行操作")
        self.textEdit.move(10, 25)
        self.textEdit.resize(300, 350)

        self.button = QPushButton('1.create jospeh', self)
        self.button.move(350, 80)
        self.button.clicked.connect(lambda: self.execute('1'))
        self.button2 = QPushButton('2.the nxet kill', self)
        self.button2.move(350, 110)
        self.button2.clicked.connect(lambda: self.execute('2'))
        self.button3 = QPushButton('3.output sequence', self)
        self.button3.move(350, 140)
        self.button3.clicked.connect(lambda: self.execute('3'))
        self.button4 = QPushButton('4.reset the start and location', self)
        self.button4.move(350, 170)
        self.button4.clicked.connect(lambda: self.execute('4'))
        self.button5 = QPushButton('5.show joseph', self)
        self.button5.move(350, 200)
        self.button5.clicked.connect(lambda: self.execute('5'))
        self.button6 = QPushButton('6.exit the programme', self)
        self.button6.move(350, 230)
        self.button6.clicked.connect(lambda: self.execute('6'))


    def next_people(self):
        outperson = self.jospeh.next()
        c = outperson.name+str(outperson.num)
        self.textEdit.setPlainText (c)
    # execute 不应像文字界面一样设置循环

    def exit(self):
        print('退出本程序！')
        sys.exit(0)


    def reset(self):

        dialog = ResetWindow(self)
        dialog.exec_()
        step, location = dialog.get_data()
        step = int(step)
        location = int(location)
        dialog.destroy()
        self.jospeh.reset(step, location)

    def show_menu(self):
        for index, item in enumerate(self.option_list, 1):
            print(index, item[0])

    def create_jospehring(self, obj=Ring, start=0, location=0):
        self.jospeh = obj()
        readdata = ZipReader()
        reader = read_data(readdata, 'D:\pythoncode\josphering\data\peopledata.zip', 'r')
        self.jospeh.from_reader(reader)
        if self.jospeh:
            dialog = ResetWindow(self)
            dialog.exec_()
            step, location = dialog.get_data()
            step = int(step)
            location = int(location)
            dialog.destroy()
            self.jospeh.reset(start, location)

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


class ResetWindow(QDialog):
    _signal = QtCore.Signal(str)

    def __init__(self, parent=None):
        super(ResetWindow, self).__init__(parent)
        self.setWindowTitle('start 和 location的设置')
        self.resize(500, 400)
        self.line1 = QLineEdit(self)
        self.line1.move(10, 25)
        self.line1.resize(100, 10)
        self.line2 = QLineEdit(self)
        self.line2.move(30, 50)
        self.line2.resize(100, 10)
        layout = QVBoxLayout(self)

        buttons = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)



    def get_data(self):
        text1 = self.line1.text()
        text2 = self.line2.text()
        return text1, text2





if __name__ == '__main__':

    app = QApplication(sys.argv)
    obj = QtInterface()
    obj.show()
    sys.exit(app.exec_())