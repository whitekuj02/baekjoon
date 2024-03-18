from collections import deque
import sys

def push(queue, i):
    queue.append(i)

def pop(queue):
    if len(queue) == 0:
        return(-1)
    else:
        return queue.popleft()

def size(queue):
    return len(queue)

def empty(queue):
    if len(queue) == 0:
        return(1)
    else:
        return(0)

def front(queue):
    if len(queue) == 0:
        return(-1)
    else:
        return(queue[0])

def back(queue):
    length = len(queue)
    if length == 0:
        return(-1)
    else:
        return(queue[length-1])


func_dict = {
    "push" : push,
    "pop" : pop,
    "size" : size,
    "empty" : empty,
    "front" : front,
    "back" : back
}

if __name__ == "__main__":
    num = int(sys.stdin.readline())
    queue = deque()

    for _ in range(num):
        data = sys.stdin.readline().split()
        
        if len(data) > 1 : # push
            func, i = data[0], int(data[1])
            func_dict[func](queue, i)
        else:
            print(func_dict[data[0]](queue))

        