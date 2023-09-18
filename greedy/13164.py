n, k = map(int, input().split())

kinders = list(map(int, input().split()))
kinders.sort()
if k == 1:
    print(kinders[-1] - kinders[0])
    exit(0)


temp = []
for i in range(n - 1):
    temp.append(kinders[i + 1] - kinders[i])

temp.sort()
if temp:
    print(sum(temp[:((k-1)*-1)]))
else:
    print(0)
