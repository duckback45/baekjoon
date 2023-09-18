from sys import stdin

n = int(input())
a = list(map(int,stdin.readline().rstrip()))
b = list(map(int,stdin.readline().rstrip()))

def toggle(index):
        if index - 1 >= 0:
            a[index - 1] ^= 1
        a[index] ^= 1
        if index + 1 < n:
            a[index + 1] ^= 1
count = 0
while True:
    for i in range(n):
        if a[i] != b[i]:
            toggle(i)
            count += 1

    if a == b:
        break
    if n > n*3:
        break
        print(-1)
        exit(0)

print(count)