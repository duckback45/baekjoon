# n = int(input())
#
# milk = [*map(int, input().split())]
#
# routine_milk = 0
# count = 0
# for m in milk:
#     if m == routine_milk:
#         count += 1
#         if routine_milk == 2:
#             routine_milk = 0
#         else:
#             routine_milk += 1
#
# print(count)


# c = 0
# for s in [*map(int, open(0).read().split())][1:]:
#     if s == c % 3:
#         c += 1
# print(c)

print([*map(int, open(0).read().split())][1:])