n, k = map(int, input().split())
hps = input()

h = 0
p = 0
count = 0
for hp in hps:
    if hp == 'P':
        if h:
            count += 1
        else:
            p += 1

    else:
        if p:
            count += 1
        else:
            h += 1

        h -= 1
