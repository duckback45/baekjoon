#수들의 합

s = int(input())
number = 0
count = 0
for i in range(1, 4294967295):
    if number > s:
        break
    number += i
    count += 1


print(count -1)