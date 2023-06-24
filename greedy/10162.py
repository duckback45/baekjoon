#전자레인지 https://www.acmicpc.net/problem/10162

'''
button = [300, 60, 10]
time = int(input())
result = []
if (time % 10 != 0):
    print(-1)
else:
    for i in button :
        result.append(time // i)
        time  = time % i
print(*result)
'''
def solution(time):
    button = [300, 60, 10]
    result = []
    if (time % 10 != 0):
        print(-1)
    else:
        for i in button :
            result.append(time // i)
            time  = time % i
    print(*result)



if __name__ == "__main__":
    solution(100)