
max = 100
list = [i for i in range(0, 1001)]
for k in range(0, 1001):
    if max < list[k]:
        break
    if list[k] == 0:
        k += 1
        continue
    if list[k] == 1:
        list[k] = 0
        k += 1
        continue
    for j in range(k, 1001, k):
        if list[j] == 0:
            continue
        if list[j] % list[k] == 0 and list[j] != list[k]:
            list[j] = 0
    k += 1


num = int(input())

data = input().split()
add = 0
for i in range(0, len(data)):
    data[i] = int(data[i])
    if list[data[i]] != 0:
        add += 1
print(add)