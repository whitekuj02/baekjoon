
import collections
num = int(input())

data = collections.deque([i for i in range(1, num+1)])

while len(data) > 1:
    data.popleft()
    data.rotate(-1)

print(data[0])