#전자레인지
T = int(input())
time = [300, 60, 10]
result = []
for i in time:
    result.append(T//i)
    T = T%i
print(T)
if T == 0:
    print(*result)
else:
    print(-1)