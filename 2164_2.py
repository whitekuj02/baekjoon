from collections import deque

if __name__ == "__main__":
    num = int(input())

    card = deque([i for i in range(1, num+1)])
    length = len(card)
    count = 1

    while (length > 1):
        if count % 2 == 0:
            card.append(card.popleft())
        else:
            card.popleft()
            length -= 1
        count += 1
    
    print(card[0])