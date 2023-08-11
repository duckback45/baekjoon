#설탕배달

n = int(input())
desc = [5, 3]
asc = [3, 5]
append = []
def solution(sugars, package):
    count = 0
    for sugar in sugars:
        for 
        count += package // sugar
        package = package % sugar

    if package != 0:
        count = 5001
    return count

result1 = solution(desc, n)
result2 = solution(asc, n)

if result1 == 5001 and result2 == 5001:
    print(-1)
else:
    print(min(result1, result1))

