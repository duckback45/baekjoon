n = int(input())
word = input()
count = 0
i = 0

# while i < n:
#     if word[i] == 'S':
#         i += 1
#         count += 1
#     elif word[i] == 'L':
#         i += 2
#         count += 1
#
# print(min(n, count+1))

LL_COUNT = word.count('LL')

if LL_COUNT <= 2:
    print(n)
else:
    print(n - LL_COUNT)