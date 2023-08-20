n = int(input())

houses = list(map(int, input().split()))
aa = sum([houses[(n//2) - 1]] * n)
bb = sum([houses[n//2]] * n)
sum_houses = sum(houses)

if abs(sum_houses - aa) <= abs(sum_houses - bb):
    print(houses[(n//2) - 1])
else:
    print(houses[(n//2)])