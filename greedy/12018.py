n, m = map(int, input().split())

possible_lecture = []
for _ in range(n):
    p, l = map(int, input().split())
    lecture = list(map(int, input().split()))
    lecture.sort(reverse=True)
    if p >= l:
        possible_lecture.append(lecture[l-1])
    else:
        possible_lecture.append(1)

possible_lecture.sort()
count = 0
for p in possible_lecture:
    if m - p < 0:
        break
    m -= p
    count += 1

print(count)