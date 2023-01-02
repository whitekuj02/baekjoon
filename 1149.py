num = int(input())

data = list(map(int, input().split()))
for i in range(1, num):
    in_data = list(map(int, input().split()))
    data_copy = data.copy()
    data[0] = min(in_data[0] + data_copy[1], in_data[0] + data_copy[2])
    data[1] = min(in_data[1] + data_copy[0], in_data[1] + data_copy[2])
    data[2] = min(in_data[2] + data_copy[1], in_data[2] + data_copy[0])

print(min(data))


