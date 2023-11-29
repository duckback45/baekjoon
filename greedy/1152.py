word = input()

word = word.lstrip()
word += ' '
count = 0
for i in range(1, len(word)):
    if word[i-1] != ' ' and word[i] == ' ':
        count += 1

print(count)