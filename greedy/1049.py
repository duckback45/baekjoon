n, m = map(int, input().split())

guitar_strings = []
min_six_package = 1001
min_each_price = 1001

for _ in range(m):
    package, each = map(int, input().split())

    min_six_package = min(package, min_six_package)
    min_each_price = min(each, min_each_price)


print(min(((min_six_package * (n//6)) + min_each_price * (n % 6)), (min_each_price * n), (min_six_package * ((n//6) + 1))))


