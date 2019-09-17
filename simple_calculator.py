def add(*args): return sum(args)

def multiply(*args): return reduce(lambda x, y: x * y, args)