from typing import List
from person import Person
import copy


class Ring(object):
    MAX_SIZE = 1000

    # typing会进行参数提醒但不会报错
    def __init__(self):
        self.step = 1
        self.start = 0
        self._ring = []
        self._temp = []
        self._current_id = 0

    # 依赖注入使得内层能够调用外层
    def from_reader(self, reader: List[Person]):
        if reader:
            for each in reader:
                self._ring.append(each)

    def is_empty(self) -> bool:
        return len(self._temp) == 0

    def pop(self, index: int):
        return self._ring.pop(index)

    def query_list(self):
        return self._ring

    def reset(self, step: int, location: int) -> None:
        self.step = step
        self.start = location-1
        self._current_id = self.start
        self._temp = copy.deepcopy(self._ring)
        return

    def next(self) -> Person:
        if self.is_empty() is True:
            raise Exception('环为空')
        size = len(self._temp)
        id = (self._current_id+(self.step-1)) % size
        outelem = self._temp.pop(id)
        self._current_id += (self.step - 1)
        return outelem

    def popelem(self):
        step = self.step
        temp = self._temp
        location = self.start % len(temp)
        if self.is_empty() is True:
            raise Exception('环为空')

        for each in range(0, len(temp)):
            location = (location + (step-1)) % len(temp)
            outelem = temp.pop(location)
            yield outelem

    def append(self, obj: Person) -> None:
        if len(self._ring) > Ring.MAX_SIZE:
            raise Exception("out of range")
        self._ring.append(obj)