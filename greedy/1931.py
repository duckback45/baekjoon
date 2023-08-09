#회의실 배정
n = int(input())
meeting = [[*map(int, input().split())] for _ in range(n)]

meeting = sorted(meeting, key=lambda x:x[1])
result = []
result.append(meeting[0][1])
for i in range(1, len(meeting)):
    if result[-1] <= meeting[i][0]:
        result.append(meeting[i][1])

print(len(result))

sel