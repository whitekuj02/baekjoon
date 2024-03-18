from collections import deque

if __name__ == "__main__":
    N, K = map(int,input().split())

    table = deque(range(1,N+1))
    result = []

    while(len(table) > 0):
        for _ in range(K-1):
            table.append(table.popleft())
        result.append(str(table.popleft()))
    
    str_result = "<" + ", ".join(result) + ">"
    print(str_result)