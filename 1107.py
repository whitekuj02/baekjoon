import sys

class controller:
    def __init__(self, n, broken_num):
        self.n = n
        self.broken_num = broken_num
        self.now = 100
    
    def forward(self):
        # 방법
        # 그냥 하나씩 더하고 빼서 점프 값 구하고 len + 더하고 뺀 만큼 하면 결과
        # 위로 가는거랑 아래로 가는거 비교는 해야 할 듯
        click_100 = abs(self.n-self.now)

        down_num = self.n
        down_click = 0
        down_possible = True
        while (not all(digit not in self.broken_num for digit in [int(i) for i in list(str(down_num))])):
            if down_num == 0:
                down_possible = False
                break
            else :
                down_num -= 1
                down_click += 1
        down_click += len(str(down_num))

        up_num = self.n
        up_click = 0
        up_possible = True
        while (not all(digit not in self.broken_num for digit in [int(i) for i in list(str(up_num))])):
            if up_click < max(down_click,click_100):
                up_num += 1
                up_click += 1
            else :
                up_possible = False
                break
        up_click += len(str(up_num))

        result = [click_100]
        if down_possible:
            result.append(down_click)
        if up_possible:
            result.append(up_click)
        return min(result)

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    broken = int(input())
    if broken > 0:
        broken_num = [int(i) for i in input().rstrip().split(' ')]
    else :
        broken_num = []

    c = controller(n,broken_num)
    print(c.forward())

