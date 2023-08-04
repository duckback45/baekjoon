n = int(input())

a = [*map(int, input().split())]
b = [*map(int, input().split())]

a.sort()
b.sort(reverse=True)

ab = [a[i] * b[i] for i in range(n)]
print(sum(ab))