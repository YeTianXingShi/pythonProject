
from Main.chche_test import *


def add_log(func):
    def wrapper():
        print("start")
        func()
        print("end")
    return wrapper


@add_log
def go1():
    fib1(400)


go1()
