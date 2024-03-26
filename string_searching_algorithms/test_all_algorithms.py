import algorithm_KMP as kmp
import algorithm_N as n
from random import randint
import algorithm_KR as kr


def rand_str():
    amount_str = randint(1, 51)
    str = ""
    for i in range(amount_str):
        choice = randint(1, 2)
        if choice == 1:
            str += "A"
        else:
            str += "B"
    return str


def test_all():
    for i in range(10000):
        text = rand_str()
        string = rand_str()
        assert kmp.find(string, text) == n.find(string, text)
        assert kr.find(string, text) == n.find(string, text)
        assert kmp.find(string, text) == kr.find(string, text)