import math

gcd, lcm = map(int, input().split())

num = int(gcd*lcm)

num1 = gcd
num2 = int(num/num1)

data1 = num1
data2 = num2
min = num1+num2
while num1 < num2:
    if num % num1 == 0 and min > num1+num2:
        if math.gcd(num1, num2) == gcd:
            data1 = num1
            data2 = num2
            min = num1 + num2
    num1 += gcd
    num2 = int(num/num1)

print(data1, end=" ")
print(data2)