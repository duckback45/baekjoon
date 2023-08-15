n, m = map(int, input().split())

from_matrix = []
to_matrix = []
check_count = 0
for _ in range(n):
    from_matrix.append([*map(int, input())])

for _ in range(n):
    to_matrix.append([*map(int, input())])

if n >= 3 and m >= 3:
    for i in range(n-2):
        for j in range(m-2):
            if i > n - 2 or j < n - 2:
                if ''.join(from_matrix[i][j:j + 2]) != ''.join(to_matrix[i][j:j + 2]):
                    check_count += 1





            # if check_flag:
            #     from_matrix[i][j:j + 3]
            #     from_matrix[i + 1][j:j + 3]
            #     from_matrix[i + 2][j:j + 3]
else:
    print(-1)