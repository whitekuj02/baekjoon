import sys

num = int(sys.stdin.readline())

data = [0] * 10001
for _ in range(0, num):
    data[int(sys.stdin.readline())] += 1

result = 0
for i in data:
    for k in range(0, i):
        print(result)
    result+=1