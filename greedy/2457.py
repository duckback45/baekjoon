import heapq

n = int(input())

flowers = []
for _ in range(n):
    f = list(map(int, input().split()))
    flowers.append([f[0]*100 + f[1], -(f[2] * 100 + f[3])])

flowers.sort()

end_date = 301
start_date = 301
index = 0
count = 0
temp = []
result = []
print(*flowers)

while flowers:
    if start_date >= flowers[0][0]:
        if end_date < -flowers[0][1]:
            if temp:
                heapq.heappop(temp)
            heapq.heappush(temp, -flowers[0][1])
            end_date = -flowers.pop(0)[1]
        else:
            flowers.pop(0)
    else:
        result.append(temp.pop())
        # flowers.pop(0)
        start_date = end_date

print(len(result) + len(temp))