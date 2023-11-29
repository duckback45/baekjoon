n = int(input())

ab = []
for _ in range(n):
    ab.append([*map(int, input().split())])


l, p = map(int, input().split())

print(*ab)