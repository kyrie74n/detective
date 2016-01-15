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

    def get_vector(self, d=None):
        v = ""
        if d is None:
            for i in range(12):
                v += letter(self.digits[i])
                if i % 2 is 1:
                    v += "-"
            return v.rstrip("-")
        else:
            for i in range(12):
                if i is d:
                    v += "?"
                else:
                    v += letter(self.digits[i])
                if i % 2 is 1:
                    v += "-"
            return v.rstrip("-")

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

    def dump(self):
        return self.indicator["array"] + self.indicator["array2"]

    def score(self):
        a = reduce(lambda x, y: x+y, self.indicator["array"])
        b = reduce(lambda x, y: x+y, self.indicator["array2"])
        return a + b
