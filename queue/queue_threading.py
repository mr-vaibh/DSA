from collections import deque

from time import sleep
from threading import Thread

# Using threading :)

queue = deque()

orders = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']

def order_food():
    for i in orders:
        queue.appendleft(i)
        print('Ordered:', queue[0])
        sleep(0.5)

def serve_food():
    sleep(1)

    while True:
        if len(queue) == 0:
            return
        print('Served:', queue.pop())
        sleep(2)


ordering_thread = Thread(target=order_food)
serving_thread = Thread(target=serve_food)

ordering_thread.start()
serving_thread.start()

ordering_thread.join()
serving_thread.join()