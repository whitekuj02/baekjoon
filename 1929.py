import math
num1, num2 = input().split()

num1 = int(num1)
num2 = int(num2)

max = int(math.sqrt(num2))

list = [i for i in range(0, num2+1)]


for k in range(0, num2):
    if max < list[k]:
        break
    if list[k] == 0:
        k += 1
        continue
    if list[k] == 1:
        list[k] = 0
        k += 1
        continue
    for j in range(k, num2+1, k):
        if list[j] == 0:
            continue
        if list[j] % list[k] == 0 and list[j] != list[k]:
            list[j] = 0
    k += 1

for i in range(num1, num2+1):
    if list[i] != 0:
        print(list[i])

