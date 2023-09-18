n = int(input())

l = []
for n in range(n):
    l.append(int(input()))

l.sort(reverse=True)

max_l = l[0]
result = 0
for i in range(1,n):
   if l[i-1] < sum(l[i:i+2]):
       result = l[i-1] + sum(l[i:i+2])
       break
if result == 0:
    print(-1)
else:
    print(result)