import math

def distance(x_1, y_1, x_2, y_2):
    n1 = pow((x_1 - x_2),2)
    n2 = pow((y_1 - y_2),2)
    return math.sqrt(n1+n2)

if __name__ == "__main__":
    num = int(input())

    for _ in range(num):
        x_1, y_1, r_1, x_2, y_2, r_2 = map(int, input().split())


        dis  = distance(x_1, y_1, x_2, y_2)

        max_ = max([dis, r_1, r_2])
        sum_ = sum([dis, r_1, r_2])
        # 점이 겹칠 때 
        if dis == 0:
            if r_1 != r_2:
                print(0)
            else:
                print(-1)
        else:
            # 삼각형이 되기 위한 조건 : 제일 긴거가 나머지 두 합보다 작아야 한다.
            if max_ < sum_ - max_:
                print(2)
            elif max_ == sum_ - max_:
                print(1)
            else:
                print(0)


        

        