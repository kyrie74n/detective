import random

__author__ = 'k'


def generate_vector():
    hoge = random.randrange(25)
    return "XX-XX-XX-XX-XX-XX"


def generate_random_vector():
    return random_letter() + random_letter() + "-" \
        + random_letter() + random_letter() + "-" \
        + random_letter() + random_letter() + "-" \
        + random_letter() + random_letter() + "-" \
        + random_letter() + random_letter() + "-" \
        + random_letter() + random_letter()

def random_letter(order=None):
    if order is None:
        return chr(65 + random.randrange(24))
    else:
        return chr(65 + order)
