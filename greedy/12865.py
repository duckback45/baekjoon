n, k = map(int, input().split())
dp = [[0] * (k + 1) for _ in range(n + 1)]
array = list(map(int, input().split()) for _ in range(n))

#물품의 수, 버틸수 있는 무게가 1부터 시작
#물건 하나씩 비교하면서
for i in range(1, n + 1):
    # weight, value = map(int, input().split())
    weight, value = array[i - 1]
    for j in range(1, k + 1):
        if j < weight:
            dp[i][j] = dp[i - 1][j]
        else:
            # 이전 물건 가치, 이전 물건 가치 + 현재 물건 가치 중 가장 큰 가치
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)

print(dp[n][k])