a, b, c, m = map(int, input().split())

if a > m:
    print(0)
    exit(0)

total_a = 0
result = 0
for _ in range(24):
    if m < total_a + a:
        if total_a - c < 0:
            total_a = 0
        else:
            total_a -= c
    else:
        total_a += a
        result += b

print(result)