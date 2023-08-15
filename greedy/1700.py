n, k = map(int, input().split())
use_order = [*map(int, input().split())]

multitap_index = [[] * 1 for _ in range(k + 1)]
use = use_order[:n]

def pickup_powercode():
    min_index = k+1
    return_u = 0
    for u in use:
        if len(multitap_index[u]) <= 1:
            return u
        else:
            if multitap_index[u][0] < min_index:
                min_index = multitap_index[u][0]
                return_u = u
    return return_u

for i in range(n, len(use_order)):
    k = use_order[i]
    multitap_index[k].append(i)

count = 0
for u in use_order[n:]:
    if u not in use:
        code = pickup_powercode()
        count += 1
        if len(multitap_index[code]) != 0:
            multitap_index[code].pop()
        use.remove(code)
        use.append(u)

print(count)