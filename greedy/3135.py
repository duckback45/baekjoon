a, b = map(int, input().split())
n = int(input())

result = abs(a-b)
buttons = []
for _ in range(n):
    buttons.append(int(input()))

for buttons in buttons:
    result = min((abs((b-buttons))+1), result)

print(result)