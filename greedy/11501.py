#주식
t = int(input())
stocks = []
for _ in range(t):
    n = int(input())
    stocks.append([*map(int, input().split())])
for stock in stocks:
    result = 0
    max_value = stock[-1]
    for s in stock[::-1]:
        if s < max_value:
            result += max_value - s
        else:
            max_value = s
    print(result)
