import sys
n = int(sys.stdin.readline())

list_child = list(map(int, sys.stdin.readline().split()))
numbers = [0] * (n + 1)

max_value = 0
for i in range(n):
    idx = list_child[i]
    numbers[idx] = numbers[idx - 1] + 1
    max_value = max(numbers[idx], numbers[idx - 1] + 1)

print(n - max_value)