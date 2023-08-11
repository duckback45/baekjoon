n = int(input())

ropes = [int(input()) for _ in range(n)]
ropes.sort(reverse=True)
result = 0

for i in range(n):
    result = max(result, (ropes[i] * (i + 1)))

print(result)