import sys

num = int(sys.stdin.readline())

data = []

for i in range(0, num):
    data.append(list(map(int, sys.stdin.readline().split())))

data = sorted(data, key=lambda x: (x[0],x[1]))

for i in data:
    print(*i)


