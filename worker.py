import json
import requests
import threading
import util
from functools import reduce

__author__ = 'k'

class Worker(threading.Thread):
    def __init__(self, num, loop):
        super(Worker, self).__init__()
        self.num = num
        self.loop = loop
        self.vector = util.Vector()
        self.score = 0
        self.code = ""
        self.state = []

    def request(self, input_vector):
        payload = {'code': input_vector}
        headers = {"X-Requested-With": "XMLHttpRequest"}
        res = requests.post("http://xxx.jp/test_last/code.php",
                            data=json.dumps(payload),
                            headers=headers)

        result = json.loads(res.text.strip("()"))

        point = reduce(lambda x, y: x+y, result["array"]) + reduce(lambda x, y: x+y, result["array2"])

        if self.score < point:
            self.score = point
            self.code = input_vector
            print("score {0}: code: {1}".format(self.score, input_vector))

    def run(self):
        for i in range(self.loop):
            self.request(self.vector.get_vector())
