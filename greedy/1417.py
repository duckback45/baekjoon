import heapq

n = int(input())

no_1 = int(input())

heap = []
for _ in range(n - 1):
    candidate = int(input())
    if no_1 <= candidate:
        heapq.heappush(heap, candidate * -1)

result = 0
while heap:
    c = heapq.heappop(heap)
    if c * -1 >= no_1:
        no_1 += 1
        result += 1
        heapq.heappush(heap, c + 1)

print(result)