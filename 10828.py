import sys

num = int(sys.stdin.readline())

data = []
for _ in range(0, num):
    in_data = sys.stdin.readline().split()
    if len(in_data) > 1:
        in_data[1] = int(in_data[1])
    data.append(in_data)
def push(num):
    stack.append(num)
def pop():
    if len(stack) > 0:
        pop_num = stack.pop()
        print(pop_num)
    else:
        print(-1)
def top():
    if len(stack) > 0:
        pop_num = stack.pop()
        print(pop_num)
        stack.append(pop_num)
    else:
        print(-1)
def size():
    size_stack = len(stack)
    print(size_stack)
def empty():
    if len(stack) == 0:
        print(1)
    else:
        print(0)

func = { "push": push,
         "pop": pop,
         "top": top,
         "size": size,
         "empty": empty,
         }
stack = []
for i in data:
    if i[0] == "push":
        func[i[0]](i[1])
    else:
        func[i[0]]()

