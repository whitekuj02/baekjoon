num = int(input())

data = list(map(int, input().split()))

data_sort = data.copy()
data_sort.sort()

for i in range(0, num):
    a = data_sort.index(data[i])
    data_sort[a] = 0
    print(a, end=" ")