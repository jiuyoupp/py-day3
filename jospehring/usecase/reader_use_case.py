from typing import List
from person import Person


# 统一接口
def read_data(obj, path: str, mode: str) -> List[Person]:
    return obj.reader(path, mode)