from typing import Any


class Reader(object):
    def read(self, path: str, mode: str) -> Any:
        raise NotImplementedError("子类没有reader方法")