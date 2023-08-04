#강의실배정
import heapq

n = int(input())
st = list([*map(int, input().split())] for _ in range(n))
st = sorted(st,  key=lambda x: x[1])
heap = []
for i in range(n):
    heapq.heappush(heap, -heapq.heappop(jewelleries)[1])

