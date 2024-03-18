from collections import deque

if __name__ == "__main__":
    data = input()
    word = deque(list(data))
    result_deque = deque()

    if len(word) == 0 : # 입력없으면 끝
        print("Error!")
        exit()
    
    w = word.popleft()
    if w.isupper() or w == "_": # 첫문자는 따로
        print("Error!")
        exit()
    else:
        result_deque.append(w)

    if '_' in word and data.islower(): #cpp
        while(len(word)>0):
            w = word.popleft()
            if w == "_":
                if len(word) == 0: # 맨뒤가 _면 에러
                    print("Error!")
                    exit()
                next_w = word.popleft()
                if next_w == "_": # 연속으로 _가 오면 에러
                    print("Error!")
                    exit()
                result_deque.append(next_w.upper())
            else:
                result_deque.append(w)
        print("".join(result_deque))

    elif not data.islower() and not '_' in word: #java
        while(len(word)>0):
            w = word.popleft()
            if w.isupper():
                result_deque.append("_")
                result_deque.append(w.lower())
            else:
                result_deque.append(w)
        print("".join(result_deque))

    elif data.islower():
        print(data)
    else:
        print("Error!")
    
