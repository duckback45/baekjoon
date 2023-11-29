n = int(input())

cows = []
for _ in range(n):
    cows.append(list(map(int, input().split())))

cows.sort()

wait_time = 0
for c in cows:
    if c[0] >= wait_time:
        wait_time = c[0] + c[1]
    else:
        wait_time += c[1]

print(wait_time)