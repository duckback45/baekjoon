# n = int(input())

# weight = []
weight = [3, 1 ,6 ,2 ,7 ,30 ,1]
# weight = [*map(int, input().split())]

weight.sort()

thing = 1
for i in range(1, len(weight)):
    numbers = {weight[i]}
    for j in weight[i:]:
        w = weight[i] + j
        if w > i:
            break
        numbers.add(w)
        numbers = w

    if thing != w:
        print(thing)

    thing += 1
