num = int(input())

data = []
for i in range(0, num):
    in_data = input().split()
    data.append(in_data)

for i in range(0, num):
    print("Case #{}:".format(i+1), end=" ")
    data[i].reverse()
    for k in data[i]:
        print(k, end=" ")
    print()
