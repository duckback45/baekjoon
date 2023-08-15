def solution(number, k):
    count = k
    temp = []
    for item in number:
        # item 값이 배열의 마지막 값보다 크면 pop
        while temp and item > temp[-1] and count > 0:
            temp.pop()
            count -= 1

        temp.append(item)

    if count > 0:
        temp = temp[:-count]

    answer = ''.join(temp)
    return answer

n, k = map(int, input().split())
num = input()

print(solution(num, k))