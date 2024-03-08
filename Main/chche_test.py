from cachetools import cached, LRUCache


# speed up calculating Fibonacci numbers with dynamic programming

def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)


@cached(cache={})
def fib1(n):
    return n if n < 2 else fib1(n - 1) + fib1(n - 2)


@cached(cache=LRUCache(maxsize=64))
def fib2(n):
    return n if n < 2 else fib2(n - 1) + fib2(n - 2)
