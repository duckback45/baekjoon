#1202 보석도둑
import heapq

# n, k = map(int, input().split())
# jewelleries = sorted([[*map(int,input().split())] for _ in range(n)], key=lambda x: -x[1])
jewelleries = [[1,65],[5,23],[2,99]]
# bags = sorted([int(input()) for _ in range(k)], key=lambda x: x)
bags = [10,2]

jewelleries.sort()
bags.sort()

values = 0
heap = []

for maximum in bags:
    while jewelleries and jewelleries[0][0] <= maximum:
        heapq.heappush(heap, -heapq.heappop(jewelleries)[1])
    if heap:
        values -= heapq.heappop(heap)

print(values)


