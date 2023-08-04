#회의실 배정

n = int(input())
times = [[*map(int, input().split())] for _ in range(n)]

print(*times)