t = int(input())

for _ in range(t):
    n = int(input())
    a = input()
    b = input()

    a_B_count = 0
    a_W_count = 0

    for i in range(n):
        if a[i] != b[i]:
            if a[i] == 'B':
                a_B_count += 1
            elif a[i] == 'W':
                a_W_count += 1

    print(max(a_B_count, a_W_count))

