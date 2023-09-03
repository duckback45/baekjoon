n = int(input())

rank = []
for _ in range(n):
    rank.append(int(input()))

rank.sort()
result = 0
for idx, r in enumerate(rank):
    result += abs(r - (idx + 1))

print(result)