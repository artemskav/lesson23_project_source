def solution_query(cmd, value, file):
    if cmd == 'filter':
        res = filter(lambda x: value in x, file)
        return res
    elif cmd == 'map':
        value = int(value)
        res = map(lambda x: x.split(" ")[value], file)
        return res
    elif cmd == 'unique':
        res = list(set(file))
        return res
    elif cmd == 'sort':
        if value == "desc":
            return sorted(file, reverse=True)
        return sorted(file)
    elif cmd == 'limit':
        value = int(value)
        res = list(file)[:value]
        return res
