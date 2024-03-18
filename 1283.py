from collections import deque

if __name__ == "__main__":
    num = int(input())
    sentence_list = []
    shorted = []

    for _ in range(num):
        sentence_list.append(input())

    for sentence in sentence_list:

        word = list(map(list,sentence.split()))
        
        result = ""
        # 1번 조건
        condition_1 = False
        condition_1_word_index = -1
        for idx, w in enumerate(word):
            if w[0].upper() not in shorted and not condition_1:
                shorted.append(w[0].upper())
                condition_1 = True
                condition_1_word_index = idx
        
        # 2번 조건
        condition_2 = False
        condition_2_word_index = -1
        condition_2_char_index = -1
        if not condition_1:
            for idx, w in enumerate(word):
                for c in range(1,len(w)):
                    if w[c].upper() not in shorted and not condition_2:
                        shorted.append(w[c].upper())
                        condition_2 = True
                        condition_2_word_index = idx
                        condition_2_char_index = c

        result = ""
        if condition_2:
            for w in range(0,condition_2_word_index):
                result += "".join(word[w]) + " "
            
            result += "".join(word[condition_2_word_index][:condition_2_char_index]) + "[" + word[condition_2_word_index][condition_2_char_index] + "]" + "".join(word[condition_2_word_index][condition_2_char_index+1:]) + " "
            
            for w in range(condition_2_word_index+1,len(word)):
                result += "".join(word[w]) + " "

        elif condition_1:
            for w in range(0,condition_1_word_index):
                result += "".join(word[w]) + " "
            
            result += "[" + word[condition_1_word_index][0] + "]" + "".join(word[condition_1_word_index][1:]) + " "
            

            for w in range(condition_1_word_index+1,len(word)):
                result += "".join(word[w]) + " "

        else:
            for w in range(0,len(word)):
                result += "".join(word[w]) + " "
        
        print(result)