import json
import requests
import threading
import util
import queue
from functools import reduce

__author__ = 'k'

class Worker(threading.Thread):
    def __init__(self, num, loop, initial_vector=None):
        super(Worker, self).__init__()
        self.num = num
        self.loop = loop
        self.vector = util.Vector(initial_vector)
        self.score = 0
        self.code = ""
        self.queue = queue.Queue()

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
            self.queue.put(input_vector)
            print("score {0}: code: {1}".format(self.score, input_vector))

        # self.score = point
        # print("score {0}: code: {1}".format(self.score, input_vector))

    def run(self):
        # for i in range(self.loop):
        #     self.request(self.vector.get_vector())
        #     self.vector.random_vector()
        #
        # print("id:{0} score:{1} code:{2}".format(self.num, self.score, self.code))

        self.request(self.vector.get_vector())

        while not self.queue.empty():
            print("search in " + self.vector.get_vector())
            print("queue in: " + str(self.queue.qsize()))
            current = self.queue.get()

            for d in range(6):
                self.vector.set_vector(current)
                for i in range(self.loop):
                    for j in range(self.loop):
                        self.vector.update_digits(i, j, d)
                        self.request(self.vector.get_vector())
