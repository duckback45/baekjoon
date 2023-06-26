#4796 캠핑

# count = 1
# while True :
#     l, p, v = map(int, input().split())
#     if l + p + v == 0:
#         break
#     holiday = (v // p) * l
#     holiday += min(v%p, l)
#
#     print('Case {0}: {1}'.format(count, holiday))
#     count += 1

def solution(L, P, V) :
    holiday = (V//P) * L
    # holiday += V%P 이것은 틀림
    holiday += min(V%P, L) #만약 남으기간보다 활용할수 캠핑을 사용할 수 있는 기간이 짧다면 사용기간을 넣어줘야 한다.

    print(holiday)

if __name__ == '__main__' :
    assert solution(1, 3, 11) == 4