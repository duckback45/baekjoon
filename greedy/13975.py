import heapq

t = int(input())

folder = []
for _ in range(t):
    k = int(input())
    folder.append([*map(int, input().split())])

list_result = []
for files in folder:
    heap = []
    files.sort()
    result = 0
    for f in files:
        heapq.heappush(heap, f)

    while len(heap) > 1:
         a = heapq.heappop(heap)
         b = heapq.heappop(heap)
         heapq.heappush(heap, a+b)
         result += a + b

    print(result)