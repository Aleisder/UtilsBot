from random import randint
from random import choice
from string import ascii_letters
from string import digits


def generate() -> str:
    password = ''.join([choice(ascii_letters + digits) for _ in range(8)])
    for i in range(0, randint(0, 8)):
        password += choice(ascii_letters + digits)
    return str(password)
