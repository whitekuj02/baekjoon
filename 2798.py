num, M = map(int, input().split())

data = list(map(int, input().split()))

max = 0

for i in range(0, num-2):
    for k in range(i+1, num-1):
        for a in range(k+1, num):
            temp = data[i] + data[k] + data[a]
            if temp <= M and temp > max:
                max = temp

print(max)