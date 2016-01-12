import json
import requests
import threading
from functools import reduce

__author__ = 'k'

VEC = 'X-XX-XX-XX-XX-X'

class Worker(threading.Thread):
    def __init__(self, num, loop):
        super(Worker, self).__init__()
        self.num = num
        self.loop = loop
        # instantiate

    def request(self, input_vector):
        payload = {'code': input_vector}
        headers = {"X-Requested-With": "XMLHttpRequest"}
        res = requests.post("http://xxx.jp/test_last/code.php",
                            data=json.dumps(payload),
                            headers=headers)

        # print(input_vector)
        # print(res.text.strip("()"))
        result = json.loads(res.text.strip("()"))

        sum = reduce(lambda x, y: x+y, result["array"]) + reduce(lambda x, y: x+y, result["array2"])

        if sum is 72 * 2 * 3:
            print("solution:" + input_vector)

    def run(self):
        for i in range(self.loop):
            self.request(chr(65 + self.num) + VEC + chr(65 + i))
