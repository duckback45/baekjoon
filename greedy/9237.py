n = int(input())

seedlings = list(map(int, input().split()))
seedlings.sort(reverse=True)


for idx, s in enumerate(seedlings):
    seedlings[idx] = idx + 1 + s

print(max(seedlings) + 1)