import os
import zipfile
from typing import List, Callable, Tuple
from jospehring.domain.person import Person
from jospehring.domain.reader import Reader
from typing import Dict



class CsvReader(Reader):
    # csv似乎不能用utf-8
    def reader(self, path: str, mode: str) -> List[Person]:
        data = []
        with open(path, mode, encoding='gbk') as f:
            for line in f.readlines():
                line = line.rstrip()
                persondata = line.split(',')
                name = persondata[0]
                try:
                    num = int(persondata[1])
                except ValueError as e:
                    num = 0
                data.append(Person(name, num))
            return data


class TxtReader(Reader):
    def reader(self,  path: str, mode: str) -> List[Person]:
        data = []
        with open(path, mode, encoding='UTF-8') as f:
            for line in f.readlines():
                line = line.rstrip()
                persondata = line.split()
                name = persondata[0]
                try:
                    num = int(persondata[1])
                except ValueError as e:
                    num = 0
                data.append(Person(name, num))
            return data


class ReaderAbastractFactory(object):
    #  依赖注入
    strategies: Dict[str, Reader] = {}

    @staticmethod
    def init_strategies():
        """初始化工厂"""
        ReaderAbastractFactory.register('.txt', TxtReader)
        ReaderAbastractFactory.register('.csv', CsvReader)
        ReaderAbastractFactory.register('.zip', ZipReader)

    @classmethod
    def get_value(cls, filetype: str):
        readway = cls.strategies[filetype]
        if readway == '':
            raise Exception('值为空')
        return readway

    @classmethod
    def register(cls, file_type: str, strategy: Callable) -> None:
        if file_type == '':
            raise Exception('strategyType can not be null')
        cls.strategies[file_type] = strategy


class ZipReader(Reader, ReaderAbastractFactory):
    def reader(self, path: str, mode: str) -> List[Person]:
        self.init_strategies()
        z_file = zipfile.ZipFile(path, mode)
        flist = z_file.namelist()
        filepath = z_file.extract(flist[0])
        filename, filetype = self.read_filename(filepath)
        data = self.readfile(filepath, filetype, mode)
        return data

    @staticmethod
    def read_filename(path: str) -> Tuple[str, str]:
        file = os.path.splitext(path)
        filename, filetype = file
        return filename, filetype

    # 使用dict代替 if语句
    def readfile(self, filepath: str, filetype: str, mode: str) -> List[Person]:
        if filetype in super().strategies.keys():
                readdata = super().get_value(filetype)
                obj = readdata()
                data = obj.reader(filepath, mode)
                return data
        else:
            raise Exception('不能读取该数据类型')

def read_data(path: str, mode: str) -> List[Person]:
    file = os.path.splitext(path)
    ReaderAbastractFactory.init_strategies()
    _, filetype = file
    classobject = ReaderAbastractFactory.get_value(filetype)
    obj = classobject()
    return obj.reader(path, mode)








