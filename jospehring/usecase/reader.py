import os
import zipfile
from typing import List
from person import Person


class Reader(object):
    def read(self, path: str, mode: str):
        raise NotImplementedError("子类没有reader方法")


class CsvReader(Reader):
    # csv似乎不能用utf-8
    def reader(self, path: str, mode: str) -> List[Person]:
        data = []
        with open(path, mode, encoding='gbk') as f:
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
    _strategies: dict = {}

    @classmethod
    def get_value(cls, type):
        readway = cls._strategies[type]
        if readway == '':
            raise Exception('值为空')
        return readway

    @classmethod
    def register(cls, file_type, strategy):
        if file_type == '':
            raise Exception('strategyType can not be null')
        cls._strategies[file_type] = strategy


class ZipReader(Reader, ReaderAbastractFactory):
    def reader(self, path: str, mode: str) -> List[Person]:
        z_file = zipfile.ZipFile(path, mode)
        flist = z_file.namelist()
        filepath = z_file.extract(flist[0])
        filename, filetype = self.read_filename(filepath)
        data = self.readfile(filepath, filetype, mode)
        return data

    @staticmethod
    def read_filename(path: str):
        file = os.path.splitext(path)
        filename, filetype = file
        return filename, filetype

    # 使用dict代替 if语句
    def readfile(self, filepath: str, filetype: str, mode: str) -> List[Person]:
        if filetype in super()._strategies.keys():
                readdata = super().get_value(filetype)
                obj = readdata()
                data = obj.reader(filepath, mode)
                return data
        else:
            raise Exception('不能读取该数据类型')



