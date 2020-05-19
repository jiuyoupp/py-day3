from typing import List
from jospehring.domain.person import Person
from jospehring.usecase.reader import ReaderAbastractFactory
import os


# 统一接口
def read_data(path: str, mode: str) -> List[Person]:
    file = os.path.splitext(path)
    ReaderAbastractFactory.init_strategies()
    filename, type = file
    classobject = ReaderAbastractFactory.get_value(type)
    obj = classobject()
    return obj.reader(path, mode)

