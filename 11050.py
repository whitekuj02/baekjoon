num1, num2 = map(int, input().split())

up = 1
down = 1

for i in range(0, num2):
    up *= (num1-i)
    down *= i+1

print(up//down)