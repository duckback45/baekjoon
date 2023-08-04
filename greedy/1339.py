alphabet_dict = {chr(i): 0 for i in range(ord('A'), ord('Z')+1)}
def merge_word(arr):
    if len(arr) <= 1:
        return arr[0]
    arr.sort(key=len)
    back = ''
    front = ''
    min_len = min(len(s) for s in arr)
    for i in range(min_len, 0, -1):
        for s in arr:
            num = len(s) - i
            back += s[num]
    for i in range(len(arr[1]) - min_len):
        front += arr[1][i]

    return front + back


def pre_merge_word(p):
    temp_word = []
    p.sort(key=len, reverse=True)
    for w in p:
        temp_word.append(w)
        s = merge_word(temp_word)
        temp_word = []
        temp_word.append(s)
    return temp_word[0]

def update_alphabet_dict(p):
    number = 9
    for w in p:
        if alphabet_dict[w] == 0:
            alphabet_dict[w] = number
            number -= 1
            if number == 0:
                break

n = int(input())
words = []
result = []

for _ in range(n):
    input_word = input()
    words.append(input_word)

s = pre_merge_word(words)
update_alphabet_dict(s)

for word in words:
    word_num = ''
    for w in word:
        word_num += str(alphabet_dict[w])
    result.append(int(word_num))

print(sum(result))


