import sys

data = []
while True:
    in_data = list(sys.stdin.readline())
    in_data.pop()
    if len(in_data) == 1 and in_data[0] == ".":
        break
    data.append(in_data)

for i in data:
    stack = []
    for k in i:
        if k == "(" or k == "[":
            stack.append(k)
        elif k == ")":
            if len(stack) != 0:
                pop = stack.pop()
            else:
                print("no")
                break
            if pop != "(":
                print("no")
                break
        elif k == "]":
            if len(stack) != 0:
                pop = stack.pop()
            else:
                print("no")
                break
            if pop != "[":
                print("no")
                break
    else:
        if len(stack) == 0:
            print("yes")
        else:
            print("no")