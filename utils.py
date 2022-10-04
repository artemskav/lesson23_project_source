import re
from typing import Iterator, Any, Optional, List

from exception import SomeError


def solution_query(cmd: Optional[str], value: Any, file: Iterator) -> List[str]:
    if cmd == 'filter':
        return list(filter(lambda x: value in x, file))
    elif cmd == 'regex':
        #       images\/(\w+|(\w+-\w+)|.{1,})\.png
        regex = re.compile(value)
        return list(filter(lambda x: regex.search(x), file))
    elif cmd == "map":
        return list(map(lambda x: x.split(" ")[:int(value)], file))
    elif cmd == 'unique':
        return list(set(file))
    elif cmd == 'sort':
        flag = value == "desc"
        return list(sorted(file, reverse=flag))
    elif cmd == "limit":
        return list(file)[:int(value)]
    else:
        raise SomeError
