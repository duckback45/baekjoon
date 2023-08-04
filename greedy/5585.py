#5585 https://www.acmicpc.net/problem/5585
'''
changes = [500, 100, 50, 10, 5, 1]
pay = 1000 - int(input())
result = 0
for i in changes :
    result += pay // i
    pay = pay % i

print(result)
'''
def solution(pay):
    changes = [500, 100, 50, 10, 5, 1]
    pay = 1000 - pay
    result = 0
    for i in changes :
        result += pay // i
        pay = pay % i

    print(result)

if __name__ == "__main__" :
    solution(1)