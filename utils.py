def solution_query(cmd, value, file):
    if cmd == 'filter':
        return filter(lambda x: value in x, file)
    elif cmd == 'map':
        value = int(value)
        return map(lambda x: x.split(" ")[value], file)
    elif cmd == 'unique':
        return list(set(file))
    elif cmd == 'sort':
        if value == "desc":
            return sorted(file, reverse=True)
        return sorted(file)
    elif cmd == 'limit':
        value = int(value)
        return list(file)[:value]
