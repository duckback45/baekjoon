n = int(input())
crane = list(map(int, input().split()))
m = int(input())
boxs = list(map(int, input().split()))
crane.sort(reverse=True)
boxs.sort(reverse=True)
if max(boxs) > max(crane):
    print(-1)
    exit()

crane = [c for c in crane if c >= min(boxs)]
count = 0

while boxs:
    for c in crane:
        for i in range(len(boxs)):
            if c >= boxs[i]: #크레인 들수 박스의 무게가 이하인경우 pop
                del boxs[i]
                break
    count += 1

print(count)
