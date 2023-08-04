t = int(input())

exam = []
for i in range(t):
    n = int(input())
    # 점수가 아니라 순위 였다니... 문제를 잘 읽자
    exam = sorted([[*map(int, input().split())] for _ in range(n)])

    top = exam[0][1]
    count = 1
    for applicant in exam:
        if applicant[1] < top:
            count += 1
            top = applicant[1]

    print(count)

