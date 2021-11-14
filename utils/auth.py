from typing import Union
from random import choice
from string import ascii_letters, digits


def generate_key(n: int):
    sources = ascii_letters + digits
    return "".join(choice(sources) for _ in range(n))
