import sys
from collections import deque
num = int(sys.stdin.readline())

data = []
for _ in range(0, num):
    in_data = sys.stdin.readline().split()
    if len(in_data) > 1:
        in_data[1] = int(in_data[1])
    data.append(in_data)
def push_front(num):
    queue.appendleft(num)
def push_back(num):
    queue.append(num)
def pop_front():
    if len(queue) > 0:
        pop_num = queue.popleft()
        print(pop_num)
    else:
        print(-1)
def pop_back():
    if len(queue) > 0:
        pop_num = queue.pop()
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

func = { "push_front": push_front,
         "push_back": push_back,
         "pop_front": pop_front,
         "pop_back": pop_back,
         "front": front,
         "back": back,
         "size": size,
         "empty": empty,
         }
queue = deque()

for i in data:
    if i[0] == "push_front" or i[0] == "push_back":
        func[i[0]](i[1])
    else:
        func[i[0]]()

