import sys
import math
data = []

end = False
while not end:
    in_data = list(map(int, sys.stdin.readline().split()))
    i = 0
    while i < 3:
        if in_data[i] != 0:
            in_data.sort()
            data.append(in_data)
            break
        i += 1
    else:
        end = True

length = len(data)
for i in range(0, length):
    if math.pow(data[i][2], 2) == math.pow(data[i][0], 2) + math.pow(data[i][1], 2):
        print("right")
    else:
        print("wrong")