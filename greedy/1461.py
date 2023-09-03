n, m = map(int, input().split())

books = list(map(int, input().split()))
plus_books = [p for p in books if p > 0]
minus_books = [m * -1 for m in books if m < 0]

plus_books.sort(reverse=True)
minus_books.sort(reverse=True)

def max_book(plus, minus):
    if max(plus, default=0) > max(minus, default=0):
        return 0
    else:
        return 1
def cal_books(bs, isPlusMax):
    multifly = 1
    if len(bs) <= 0:
        return 0
    if isPlusMax:
        multifly = 2

    count = max(bs[:m]) * multifly

    for i in range(m, len(bs), m):
        count += max(bs[i:i+m]) * 2

    return count

if max_book(plus_books, minus_books):
    print(cal_books(plus_books, 1) + cal_books(minus_books, 0))
else:
    print(cal_books(plus_books, 0) + cal_books(minus_books, 1))
