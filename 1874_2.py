import sys

if __name__ == "__main__":
    num = int(sys.stdin.readline())

    ans = []
    for _ in range(num):
        n = int(sys.stdin.readline())
        ans.append(n)
        
    number = list(range(num,0,-1))
    stack = []

    result = []
    for i in ans:
        while(True):
            if len(stack) == 0:
                stack.append(number.pop())
                result.append("+")
            else:
                check = stack.pop() # 마지막에 뭐 있나 확인용
                if check != i:
                    stack.append(check) # 원상 복구
                    if len(number) == 0:
                        break
                    stack.append(number.pop())
                    result.append("+")
                else: # 같으면 끝
                    result.append("-")
                    break
    
    if len(stack) == 0:
        for i in result:
            print(i)
    else:
        print("NO")
        
            
                


