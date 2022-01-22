from collections import deque


def print_binaries(num):
    queue = deque()
    queue.appendleft('1')
    
    for i in range(num):
        front = queue[0]

        print("    ", front)

        queue.appendleft(front + '0')
        queue.appendleft(front + '1')
    
    return queue

print(print_binaries(10))