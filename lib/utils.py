# coding: utf-8
# email: khahux@163.com

from random import choice
from string import ascii_letters


def random_string(length=8, letters=ascii_letters):
    return ''.join(choice(letters) for _ in range(length))