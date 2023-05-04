import sys

num = int(sys.stdin.readline())

data = []
for _ in range(0,num):
    data.append(int(sys.stdin.readline()))

stack = []
for i in data:
    if i == 0 and len(stack) != 0:
        stack.pop()
    else:
        stack.append(i)

print(sum(stack))