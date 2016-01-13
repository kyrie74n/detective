import time
import worker

__author__ = 'k'

if __name__ == '__main__':
    thread_count = 4
    initial_vector = [
        "ED-JC-FI-DF-LI-AK",
        "FK-DB-LD-AW-HL-AV",
        "GG-GI-MC-AD-CK-FP",
        "OI-DT-TV-XW-AB-XQ"
    ]

    loop = 24
    threads = []
    flag = True
    start = time.time()

    for i in range(thread_count):
        threads.append(worker.Worker(i, loop, initial_vector[i]))

    for i in range(thread_count):
        threads[i].start()

    for i in range(thread_count):
        threads[i].join()

    elapsed_time = time.time() - start
    print("elapsed_time:{0}".format(elapsed_time) + "[sec]")
    print("average_time:{0}".format(elapsed_time/(thread_count * loop)) + "[sec]")
