N, M = map(int, input().split())

data = list(map(int, input().split()))

def search(start,end):
    mid = (start+end)//2

    if start > end:
        return mid

    sum = 0
    for i in data:
        if mid < i:
            sum += i - mid

    if sum > M:
        return search(mid+1, end)
    elif sum == M:
        return mid
    else:
        return search(start, mid-1)

print(search(0,max(data)))
