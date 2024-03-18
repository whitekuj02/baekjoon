

num = []
while(1):
    try:
        n1, n2 = map(int, input().split())
        num.append(n1 + n2)
    except:
        break

for i in num:
    print(i)