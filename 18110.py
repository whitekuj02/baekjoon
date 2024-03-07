import sys

class solved_ac:
    def __init__(self, n, data):
        self.n = n
        self.cut = round(n * 0.15 +  0.0000001)
        self.data = sorted(data)

    def forward(self):
        sum = 0
        num = 0
        for i in range(self.cut, self.n-self.cut):
            sum += self.data[i]
            num += 1

        if self.n == 0:
            return 0
        else :
            return round(sum/num +  0.0000001)

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    data = []
    for i in range(n):
        num = int(input())
        data.append(num)
    
    c = solved_ac(n, data)
    print(c.forward())
