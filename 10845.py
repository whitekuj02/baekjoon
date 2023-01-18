import sys
from collections import deque
num = int(sys.stdin.readline())

data = []
for _ in range(0, num):
    in_data = sys.stdin.readline().split()
    if len(in_data) > 1:
        in_data[1] = int(in_data[1])
    data.append(in_data)
def push(num):
    queue.append(num)
def pop():
    if len(queue) > 0:
        pop_num = queue.popleft()
        print(pop_num)
    else:
        print(-1)
def front():
    if len(queue) > 0:
        pop_num = queue.popleft()
        print(pop_num)
        queue.appendleft(pop_num)
    else:
        print(-1)
def back():
    if len(queue) > 0:
        pop_num = queue.pop()
        print(pop_num)
        queue.append(pop_num)
    else:
        print(-1)
def size():
    size_stack = len(queue)
    print(size_stack)
def empty():
    if len(queue) == 0:
        print(1)
    else:
        print(0)

func = { "push": push,
         "pop": pop,
         "front": front,
         "back": back,
         "size": size,
         "empty": empty,
         }
queue = deque()

for i in data:
    if i[0] == "push":
        func[i[0]](i[1])
    else:
        func[i[0]]()

