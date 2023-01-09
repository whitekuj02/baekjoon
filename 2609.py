a, b = map(int, input().split())

def GCD(a,b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    else:
        return GCD(b, a%b)

c = GCD(a,b)
print(c)
print(int((a*b)/c))