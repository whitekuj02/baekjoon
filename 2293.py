coin, cost = map(int, input().split())

data = []
for i in range(0, coin):
    data.append(int(input()))

dp = [0 for i in range(0, cost + 1)]
dp[0] = 1
for i in range(0, coin):
    for k in range(data[i], cost + 1):
        num = k - data[i]
        dp[k] += dp[num]

print(dp[cost])