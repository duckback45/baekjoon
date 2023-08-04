def word_math():
    n = int(input())
    words = [input() for _ in range(n)]
    alphabet = {}

    for word in words:
        for i in range(len(word)):
            c = word[i]
            if c not in alphabet:
                alphabet[c] = 10 ** (len(word) - 1 - i)
            else:
                alphabet[c] += 10 ** (len(word) - 1 - i)

    sorted_alphabet = sorted(alphabet.items(), key=lambda x: x[1], reverse=True)

    result = 0
    number = 9
    for char, value in sorted_alphabet:
        result += value * number
        number -= 1

    return result


answer = word_math()
print(answer)