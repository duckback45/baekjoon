n,m = map(int, input().split())

j = int(input())

apples = []
result = 0
start = 1
end = start + m - 1
for _ in range(j):
    apple = int(input())
    if apple > start and apple > end:
        result += apple - end
        end = apple
        start = end - (m - 1)
    elif apple < start and apple < end:
        result += start - apple
        start = apple
        end = start + (m - 1)
print(abs(result))