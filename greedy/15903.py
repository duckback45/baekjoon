import heapq

n, m = map(int, input().split())
cards = list(map(int, input().split()))

heap = []
for i in range(n):
    heapq.heappush(heap, cards[i])

for _ in range(m):
    two_sum_card = heapq.heappop(heap) + heapq.heappop(heap)
    heapq.heappush(heap, two_sum_card)
    heapq.heappush(heap, two_sum_card)

print(sum(heap))

