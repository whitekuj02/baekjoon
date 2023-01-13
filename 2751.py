import sys
num = int(sys.stdin.readline())

data = []
for _ in range(0, num):
    data.append(int(sys.stdin.readline()))

data = sorted(data)
for i in range(0, num):
    print(data[i])