#수 묶기
n = int(input())

plus = []
minus = []

result = 0
for i in range(n):
    num = int(input())
    if num >= 1:
        plus.append(num)
    elif num <= 0:
        minus.append(num)
    else:
        result += num

plus.sort(reverse=True)
minus.sort()

def multiply(arr):
    ans = 1
    for n in arr:
        ans *= n

    return ans


def solution(p):
    max_value = 0
    for i in range(0, len(p), 2):
        max_value += max(sum(p[i:i+2]), multiply(p[i:i+2]))
    return max_value

print(solution(plus) + solution(minus))

