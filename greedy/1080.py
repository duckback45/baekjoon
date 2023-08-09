n, m = map(int, input().split())

from_matrix = []
to_matrix = []
for _ in range(n):
    from_matrix.append([*map(int, input())])
for _ in range(n):
    to_matrix.append([*map(int, input())])

if n >= 3 and m >= 3:
    for i in range(n-2):
        for j in range(m-2):
            print(from_matrix[i][j:j+3])
            print(from_matrix[i+1][j:j+3])
            print(from_matrix[i+2][j:j+3])
else:
    print(-1)