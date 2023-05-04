num = int(input())

data = list(input())

sum = 0
jiso = 0
for i in data:
    sum += (ord(i) - 96) * pow(31, jiso)
    jiso += 1

print(sum % 1234567891)