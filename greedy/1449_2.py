n, l = map(int, input().split())
leak = list(map(int, input().split()))
leak.sort()
ans = 0
while len(leak):
    idx = 0
    while idx < len(leak):
        if leak[idx] < leak[0] - 0.5 + l:
            idx += 1
        else:
            ans += 1
            break
    del leak[:idx]
print(ans + 1)