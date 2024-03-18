


if __name__ == "__main__":
    a1, a2 = map(list,input().split())
    a1.reverse() # O(n)
    a2.reverse() # O(n)
    result = list(str(int("".join(a1)) + int("".join(a2))))
    result.reverse()
    print(int("".join(result)))
