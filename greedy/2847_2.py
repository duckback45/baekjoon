import sys
input = sys.stdin.readline
N = int(input())
arr = []
answer=0
for _ in range(N):
    arr.append(int(input()))
for i in range(len(arr)-1, 0, -1):
    if arr[i]>arr[i-1]:
        continue
    else:
        answer+=arr[i-1]-arr[i]+1
        arr[i-1]=arr[i]-1
print(answer)
