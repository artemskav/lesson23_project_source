import re
from typing import Iterator, List, Any


def solution_query(cmd: str, value: str, file: Iterator) -> List[Any]:
    if cmd == 'filter':
        return list(filter(lambda x: value in x, file))
    elif cmd == 'regex':
        regex = re.compile(r'(value)')
        return list(filter(lambda x: regex.findall(x), file))
    elif cmd == 'map':
        value = int(value)
        return list(map(lambda x: x.split(" ")[value], file))
    elif cmd == 'unique':
        return list(set(file))
    elif cmd == 'sort':
        return sorted(file, reverse=(value == "desc"))
    elif cmd == 'limit':
        value = int(value)
        return list(file)[:value]
