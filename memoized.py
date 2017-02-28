class _memoized(object):
    def __init__(self, func):
        self.func = func
        self.cache = {}
    def __call__(self, *args):
        try:
            return self.cache[args]
        except KeyError:
            self.cache[args] = value = self.func(*args)
            return value
        except TypeError:
            return self.func(*args)

def memoized(func):
    cache = {}
    def wrapped(*args):
        try:
            return cache[args]
        except KeyError:
            cache[args] = func(*args)
            return cache[args]
        except TypeError:
            return func(*args)
    return wrapped

@memoized
def fib(n):
    if n < 2:
        return 1
    return fib(n-1) + fib(n -2)

# fib = _memoized(fib)

for i in range(5):
    print fib(i)
