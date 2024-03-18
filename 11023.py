def add(i):
    result = 0
    for num in i:
        result += num
    return result

if __name__ == "__main__":
    i = list(map(int,input().split()))
    result = add(i)
    print(result)