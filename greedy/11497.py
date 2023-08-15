t = int(input())
result = []
for _ in range(t):
    n = int(input())
    log = list(map(int, input().split()))
    log.sort()

    temp = []
    temp2 = []
    for i in range(n):
        if i % 2 == 0:
            temp.append(log[i])
        else:
            temp2.append(log[i])

    log = temp + temp2[::-1]

    last = log[0]
    max_value = 0
    for l in log[1:]:
        max_value = max(abs(l - last), max_value)
        last = l

    result.append(max_value)

print(*result)
