
num1 = int(input())

data1 = input().split()
for i in range(0, len(data1)):
    data1[i] = int(data1[i])

num2 = int(input())

data2 = input().split()
for i in range(0, len(data2)):
    data2[i] = int(data2[i])

for i in range(0, num1):
    if data2[i] in data1:
        print("1")
    else:
        print("0")

