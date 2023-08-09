n = int(input())

distance = list(map(int,input().split()))
cost = list(map(int,input().split()))
cost = cost[:-1]
min_cost  = cost[0]
result = min_cost * distance[0]
for i in range(1, n - 1):
    if min_cost > cost[i]:
        result += cost[i] * distance[i]
        min_cost = cost[i]
    else:
        result += min_cost * distance[i]


print(result)