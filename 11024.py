def add(i):
    result = 0
    for num in i:
        result += num
    return result

if __name__ == "__main__":
    num = int(input())
    result_list = []
    for _ in range(0,num):
        i = list(map(int,input().split()))
        result = add(i)
        result_list.append(result)

    for r in result_list:
        print(r)