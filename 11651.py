import sys

num = int(sys.stdin.readline())

data = []
for _ in range(0, num):
    in_data = list(map(int, sys.stdin.readline().split()))
    data.append(in_data)

data.sort(key=lambda x: (x[1], x[0]))

for i in data:
    print(*i)
