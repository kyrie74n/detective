from functools import reduce
import json
import random
import requests

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
        self.indicator = None

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

    def update_digits1(self, i, param):
        self.digits[param] = i

    def update_digits2(self, i, j, param):
        self.digits[2 * param] = i
        self.digits[2 * param + 1] = j

    def request(self):
        payload = {'code': self.get_vector()}
        headers = {"X-Requested-With": "XMLHttpRequest"}
        res = requests.post("http://inspyre.jp/test_last/code.php",
                            data=json.dumps(payload),
                            headers=headers)

        self.indicator = json.loads(res.text.strip("()"))

    def diff(self, vector):
        d = []
        for i in range(len(self.indicator["array"])):
            d.append(self.indicator["array"][i] - vector.indicator["array"][i])

        for i in range(len(self.indicator["array2"])):
            d.append(self.indicator["array2"][i] - vector.indicator["array2"][i])

        return str(d)

    def score(self):
        a = reduce(lambda x, y: x+y, self.indicator["array"])
        b = reduce(lambda x, y: x+y, self.indicator["array2"])
        return a + b
