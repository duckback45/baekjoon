import sys
from heapq import heappop, heappush

input = sys.stdin.readline

n = int(input())

meetings = []
for _ in range(n):
    a, b, c = list(map(int, input().split()))
    meetings.append((b, c))

meetings.sort(key=lambda x: x[0])
heap = []
for start, end in meetings:
    if heap and heap[0] <= start:
        heappop(heap)
    heappush(heap, end)

print(len(heap))