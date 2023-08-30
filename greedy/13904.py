import heapq
import sys
from queue import PriorityQueue

N = int(sys.stdin.readline().rstrip())
arr = []
sol = PriorityQueue()
result = 0

for _ in range(N):
    d, w = map(int, sys.stdin.readline().split())
    arr.append([d, w])

# 과제를 마감일 오름차순으로 정렬
arr.sort()

# 과제의 마감일 중 가장 마지막
t = arr[N - 1][0]
heap = []
# 과제의 가장 마지막 마감일부터 거꾸로 진행
for day in range(t, 0, -1):

    # 아직 마감일이 더 짧은 과제가 남아있고,
    # 과제 중 마감일이 현재의 날짜보다 더 큰 것(마감되지 않은 과제)을 PriorityQueue에 추가
    while arr and arr[-1][0] >= day:
        # sol.put(-arr.pop()[1])
        heapq.heappush(heap, -arr.pop()[1])

    # 수행할 과제가 남아있을 때 가장 점수가 큰 과제 수행
    if len(heap) > 0:
        # result += (-sol.get())
        result += heapq.heappop(heap) * -1
print(result)