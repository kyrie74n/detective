__author__ = 'k'

import time
import worker

if __name__ == '__main__':
    thread_count = 96
    loop = 24
    threads = []
    flag = True
    start = time.time()

    for i in range(thread_count):
        threads.append(worker.Worker(i, loop))

    for i in range(thread_count):
        threads[i].start()

    for i in range(thread_count):
        threads[i].join()

    elapsed_time = time.time() - start
    print("elapsed_time:{0}".format(elapsed_time) + "[sec]")
    print("average_time:{0}".format(elapsed_time/(thread_count * loop)) + "[sec]")
