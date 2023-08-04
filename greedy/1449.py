n, l = map(int, input().split())

pipes = list(map(int, input().split()))

pipes.sort()

last_pipe = pipes[0]
count = 0
s = 0
for i in range(1, n):
    s += pipes[i] - last_pipe
    last_pipe = pipes[i]
    if s >= l:
        count += 1
        s = 0
    if i == n-1 and s <= l:
        count += 1
if n == 1:
    print(1)
else:
    print(count)
