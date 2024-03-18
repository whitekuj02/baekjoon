import sys

if __name__ == "__main__":
    num = int(sys.stdin.readline())
    result = 0
    for _ in range(0,num):
        i = int(sys.stdin.readline())
        result += i
    
    print(num)
    print(result)