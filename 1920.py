
num1 = int(input())

data1 = input().split()
for i in range(0, len(data1)):
    data1[i] = int(data1[i])

num2 = int(input())

data2 = input().split()
for i in range(0, len(data2)):
    data2[i] = int(data2[i])

data1.sort()

def search(start, end, data_list, data):
    mid = int((start + end)/2)
    if mid == start or mid == end:
        if data_list[mid] == data or data_list[mid+1] == data:
            print("1")
        else:
            print("0")
        return 0
    if data_list[mid] > data:
        search(start, mid, data_list, data)
    elif data_list[mid] < data:
        search(mid, end, data_list, data)
    else:
        print("1")

for i in range(0, num2):
    search(0, num1 - 1, data1, data2[i])
