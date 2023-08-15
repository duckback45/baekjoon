n = int(input())
input_product = []

for _ in range(n):
    input_product.append(int(input()))

input_product.sort()
product = input_product[:2] + [input_product[-1]] + input_product[2:-1]

result = 0
j = 0
for i in range(1, (n//3) + 1):
    result += product[i + j]
    j += 1
    result += product[i + j]
    j += 1
if n % 3 != 0:
    result = result + sum(product[-(n % 3):])

print(result)

