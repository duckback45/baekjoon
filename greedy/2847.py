n = int(input())

num = []
for _ in range(n):
    num.append(int(input()))

count = 0
for i in range(n-1, 0, -1):
    while num[i] <= num[i -1]:
        num[i - 1] = num[i - 1] - 1
        count += 1


print(count)