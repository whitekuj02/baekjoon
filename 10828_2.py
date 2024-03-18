import sys

def push(stack, num, leng):
    stack.append(num)
    leng += 1
    return leng

def pop(stack, leng):
    if leng > 0:
        print(stack.pop())
        leng -= 1
    else:
        print("-1")
    return leng

def empty(stack, leng):
    if leng == 0:
        print(1)
    else:
        print(0)

def top(stack, leng):
    if leng > 0:
        n = stack.pop()
        print(n)
        stack.append(n)
    else:
        print("-1")

if __name__ == "__main__":
    num = int(sys.stdin.readline())

    stack = []
    leng = 0

    for _ in range(num):
        i = sys.stdin.readline().split()
        if len(i) > 1: # push
            n = int(i[1])
            leng = push(stack, n, leng)
        else:
            if i[0] == "pop":
                leng = pop(stack, leng)
            elif i[0] == "size":
                print(leng)
            elif i[0] == "empty":
                empty(stack, leng)
            elif i[0] =="top":
                top(stack, leng)
