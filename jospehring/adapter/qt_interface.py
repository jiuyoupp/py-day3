from jospehring.adapter.interface import Interface
from jospehring.usecase.ring import Ring
from jospehring.adapter.reader import read_data
from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QWidget
from PySide2.QtWidgets import QDialog
from PySide2.QtWidgets import QFileDialog
from PySide2.QtWidgets import QMessageBox
from PySide2.QtCore import Signal
from jospehring.adapter.menu import Ui_Form
from jospehring.adapter.child import Ui_Dialog
import sys


class MyMainWindow(QWidget, Ui_Form, Interface):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.pushbutton.clicked.connect(lambda: self.execute('1'))
        self.pushbutton_2.clicked.connect(lambda: self.execute('2'))
        self.pushbutton_3.clicked.connect(lambda: self.execute('3'))
        self.pushbutton_4.clicked.connect(lambda: self.execute('4'))
        self.pushbutton_5.clicked.connect(lambda: self.execute('5'))
        self.pushbutton_6.clicked.connect(lambda: self.execute('6'))

    def next_people(self):
        try:
            outperson = next(self.jospeh)
            c = outperson.name + str(outperson.num)
            self.textedit.setPlainText(c)
        except Exception as e:
            QMessageBox.warning(self, 'warning', '环为空')

    def exit(self):
        print('退出本程序！')
        sys.exit(0)

    def opendialog(self):
        dialog = ChildWindow(self)
        dialog.Signal_OneParameter.connect(self.deal_emit_slot)
        dialog.show()
        dialog.exec_()
        dialog.destroy()

    def reset(self):
        if not self.jospeh:
            self.opendialog()

    def deal_emit_slot(self, step, location, path):
        if step.isdecimal() is True and location.isdecimal() is True:
            step = int(step)
            location = int(location)
            reader = read_data(path, 'r')
            self.jospeh.from_reader(reader)
            self.jospeh.reset(step, location)
        else:
            QMessageBox.warning(self, 'warning', '输入数字不是整数')

    def create_jospehring(self, obj=Ring, start=0, location=0):
        self.jospeh = obj()
        if not (self.jospeh is None):
            self.opendialog()

    def to_string(self, peopledata):
        outdata = ''
        for person in peopledata:
            outdata += person.name + str(person.num) + '\n'
        return outdata

    def show_jospeh(self):
        ring = self.jospeh.query_list()
        outdata = self.to_string(ring)
        self.textedit.setPlainText(outdata)

    def out_sequnece(self):
        if self.jospeh.is_empty():
            QMessageBox.warning(self, 'warning', '环为空')
        jospehring = self.jospeh
        outdata = self.to_string(jospehring)
        self.textedit.setPlainText(outdata)


    def execute(self, choice):
        if 1 <= int(choice) <= len(self.option_list):
            choice = int(choice)
            temp = callable(getattr(type(self), self.option_list[choice - 1][1]))
            if hasattr(type(self), self.option_list[choice - 1][1]) and temp is True:
                # 反射不能使用self. 的形式，将self进行传参
                ret = getattr(type(self), self.option_list[choice - 1][1])(self)
            else:
                print('方法未定义或不可调用')
        else:
            print('您输入的序号y有误，请检查后重新输入！')


class ChildWindow(QDialog, Ui_Dialog):
    Signal_OneParameter = Signal(str, str, str)

    def __init__(self, parent=None):
        super(ChildWindow, self).__init__(parent)
        self.setupUi(self)
        path, _ = QFileDialog.getOpenFileName(
            self,
            'Open file',
            'D:\\pythoncode\\josphering\\data',
            '*.txt *.csv *.zip'
        )
        self.buttonbox.accepted.connect(lambda: self.emit_signal(path))

    def emit_signal(self, path=None):
        text1 = self.lineedit.text()
        text2 = self.lineedit_2.text()
        if path == '':
            QMessageBox.warning(self, 'warning', '打开文件为空')
        else:
            self.Signal_OneParameter.emit(text1, text2, path)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    obj = MyMainWindow()
    obj.show()
    sys.exit(app.exec_())

