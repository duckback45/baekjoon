#카드정렬하기
import sys
import heapq

input = sys.stdin.readline

n = int(input())
pq = []
for i in range(n):
    heapq.heappush(pq, int(input()))

result = 0
if n == 1:
    print(0)
else:
    while pq:
        sum_value = heapq.heappop(pq)
        sum_value += heapq.heappop(pq)
        result += sum_value
        if len(pq) == 0:
            break

        heapq.heappush(pq, sum_value)
    print(result)