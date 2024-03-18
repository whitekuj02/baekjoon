import sys

if __name__ == "__main__":
    num = int(sys.stdin.readline())

    for _ in range(num):
        stack = []
        data = list(sys.stdin.readline())
        data.pop() # 마지막에 \n 들어감

        for item in data:
            if item == "(":
                stack.append("(")
            else:
                if len(stack) == 0:
                    stack.append(")")
                    break
                else:
                    stack.pop()
        
        if len(stack) > 0:
            print("NO")
        else:
            print("YES")

