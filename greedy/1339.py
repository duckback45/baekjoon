def make_flat_word(arr):
    result = ""

    min_len = min(len(s) for s in arr)

    for i in range(min_len):
        for s in arr:
            result += s[len(s) - i]

    for i in range(min_len, len(arr[0])):
        result += arr[0][i]

    return result
#
# alphabet_dict = {chr(i): 0 for i in range(ord('A'), ord('Z')+1)}
# n = int(input())
# alphabet_number = 9
#
# word = []
# max_len = 0
# for _ in range(n):
#     word.append(input())
#
#
#
# word.sort(key=len,reverse=True)
# for w in word:
#     for i in w:
#         if alphabet_dict[i] == 0:
#             alphabet_dict[i] = alphabet_number
#             alphabet_number -= 1
#
# for _ in range(n):
#     for i in word:
#         for j in i:
#             alphabet_dict[j]

print(make_flat_word(['AACC','BB']))