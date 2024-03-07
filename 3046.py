def score(R1, S):
    R2 = (S * 2) - R1
    return R2

if __name__ == "__main__":
    R1, S = input().split()
    R1, S = int(R1), int(S)
    R2 = score(R1, S)
    print(R2)