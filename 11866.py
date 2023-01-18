N, K = map(int, input().split())

data = [x for x in range(1, N+1)]

result = []
idx = K-1
for i in range(0, N):
    pop = data.pop(idx)
    result.append(pop)
    if N-i-1 == 0:
        break
    idx += K-1
    idx %= N-i-1

print("<" + ", ".join(map(str,result)) + ">")