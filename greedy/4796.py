#4796 https://www.acmicpc.net/problem/4796


case = 0
while True:
    case += 1
    count =  0
    l, p, v = map(int, input().split())
    if sum(l, p, v) > 0:
        count = l // p
        count += l % p
        print('case {0}: {1}'.format(case, count))
    else :
        break

