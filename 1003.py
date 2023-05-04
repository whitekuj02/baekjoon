import sys

num = int(sys.stdin.readline())

data = []
for _ in range(0, num):
    data.append(int(sys.stdin.readline()))


for i in data:
    dp = []
    for k in range(0, i + 1):
        if k == 0:
            dp.append([1, 0])
        elif k == 1:
            dp.append([0, 1])
        else:
            dp.append([dp[k-2][0] + dp[k-1][0],
                       dp[k-2][1] + dp[k-1][1]])
    print(str(dp[i][0]) + " " + str(dp[i][1]))
