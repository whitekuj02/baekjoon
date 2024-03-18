

if __name__ == "__main__":
    num = int(input())
    wording_list = []
    for _ in range(0,num):
        word = list(input().split())
        wording_list.append(word)
    
    for w in wording_list:
        reverse_w = []
        for i in w:
            a = "".join(list(reversed(list(i))))
            reverse_w.append(a)
        print(" ".join(reverse_w))
            