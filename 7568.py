import sys

num = int(sys.stdin.readline())

data = []
for i in range(0, num):
    in_data = list(map(int, sys.stdin.readline().split()))
    data.append(in_data)


result = []
for i in range(0, num):
    count = 1
    for k in range(0, num):
        if data[i][0] < data[k][0] and data[i][1] < data[k][1]:
            count += 1
    result.append(count)

print(*result)
