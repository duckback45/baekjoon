#회의실 배정
n = int(input())
meeting = [[*map(int, input().split())] for _ in range(n)]

meeting.sort(key=lambda x: (x[1], x[0]))

endTime = meeting[0][1]
count = 1
for i in range(1, len(meeting)):
    #result
    if endTime <= meeting[i][0]:
        endTime = meeting[i][1]
        count += 1

print(count)