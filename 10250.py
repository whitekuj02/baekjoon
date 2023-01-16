num = int(input())

data = []

for _ in range(0, num):
    in_data = list(map(int, input().split()))
    data.append(in_data)

for i in range(0, num):
    W = int(data[i][2]/data[i][0]) + 1
    H = data[i][2] % data[i][0]

    if H == 0:
        H += data[i][0]
        W -= 1

    if W < 10:
        room = str(H) + "0" + str(W)
    else:
        room = str(H) + str(W)

    print(room)

