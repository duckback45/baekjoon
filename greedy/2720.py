n = int(input())

quarter = 25
dime = 10
nickel = 5
penny = 1

for _ in range(n):
    result = []
    money = int(input())

    result.append(money // quarter)
    money = money % quarter
    result.append(money // dime)
    money = money % dime
    result.append(money // nickel)
    money = money % nickel
    result.append(money // penny)
    print(*result)

