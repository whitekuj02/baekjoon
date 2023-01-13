import sys

num = int(sys.stdin.readline())

data = []

for _ in range(0, num):
    in_data = list(sys.stdin.readline())
    in_data.pop()
    data.append(in_data)


for i in range(0, num):
    stack = []
    for k in data[i]:
        if k == "(":
            stack.append(k)
        elif len(stack) == 0 and k == ")":
            stack.append(k)
            break
        else:
            stack.pop()
    if len(stack) == 0:
        print("YES")
    else:
        print("NO")