import random

__author__ = 'k'

def letter(order=None):
    if order is None:
        return chr(65 + random.randrange(24))
    else:
        return chr(65 + order)

class Vector:
    def __init__(self, initial_vector):
        super(Vector, self).__init__()
        self.digits = []
        if initial_vector is None:
            for i in range(12):
                self.digits.append(random.randrange(24))
        else:
            for i in range(12):
                self.digits.append(0)

            self.set_vector(initial_vector)

    def set_vector(self, vector):
        v = vector.replace("-", "")
        for i in range(12):
            self.digits[i] = ord(v[i]) - 65

    def random_vector(self):
        for i in range(12):
            self.digits[i] = random.randrange(12)

    def get_vector(self):
        return letter(self.digits[0]) + letter(self.digits[1]) + "-" \
            + letter(self.digits[2]) + letter(self.digits[3]) + "-" \
            + letter(self.digits[4]) + letter(self.digits[5]) + "-" \
            + letter(self.digits[6]) + letter(self.digits[7]) + "-" \
            + letter(self.digits[8]) + letter(self.digits[9]) + "-" \
            + letter(self.digits[10]) + letter(self.digits[11])

    def update_digits(self, i, j, param):
        self.digits[2 * param] = i
        self.digits[2 * param + 1] = j
