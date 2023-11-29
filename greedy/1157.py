words = input().upper()

dict_cnt_words = {}
for w in words:
    if w not in dict_cnt_words:
        dict_cnt_words[w] = words.count(w)

dict_cnt_words = sorted(dict_cnt_words.items(), key = lambda item: item[1])

if len(dict_cnt_words) > 1:
    first_word = dict_cnt_words.pop()
    second_word = dict_cnt_words.pop()
    if first_word[1] == second_word[1]:
        print("?")
    else:
        print(first_word[0])
else:
    first_word = dict_cnt_words.pop()
    print(first_word[0])
