
def factorial(n):
    result = 1
    for i in range(n,0,-1):
        result *= i
    sum = 0
    for i in reversed(str(result)):
        if i == '0':
            sum += 1
        else :
            break
    return sum

if __name__ == "__main__":
    n = int(input())
    result = factorial(n)
    print(result)