import sys

num = int(sys.stdin.readline())

# data_age = []
# data_name = []
# for i in range(0,num):
#     in_data = sys.stdin.readline().split()
#     in_data[0] = int(in_data[0])
#
#     data_age.append(in_data[0])
#     data_name.append(in_data[1])
#
#
# for i in range(1, num):
#     for k in range(i, -1, -1):
#         if data_age[k] > data_age[i]:
#             data_age[i], data_age[k] = data_age[k], data_age[i]
#             data_name[i], data_name[k] = data_name[k], data_name[i]
#             i = k
#
# for i in range(0, num):
#     print(data_age[i], data_name[i])

data = []

for i in range(0, num):
    in_data = list(sys.stdin.readline().split())
    in_data[0] = int(in_data[0])
    data.append(in_data)

data.sort(key=lambda x: x[0])

for i in range(0, num):
    print(*data[i])