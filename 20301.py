from collections import deque

if __name__ == "__main__":
    N, K, M = map(int,input().split())

    table = deque(range(1,N+1))
    result = []

    reverse = False
    count = 0
    dead_people = 0
    while(dead_people < N):
        if not reverse:
            for _ in range(K-1):
                table.append(table.popleft())
            result.append(str(table.popleft()))
        else :
            for _ in range(K-1):
                table.appendleft(table.pop())
            result.append(str(table.pop()))
        # 제거 카운트
        dead_people += 1    
        count += 1
        count %= M
        if count == 0:
            reverse = not reverse
    
    for i in result:
        print(i)