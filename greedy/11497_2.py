for i in[*open(0)][2::2]:
    a=sorted(map(int,i.split()))

print(max(j-i for i,j in zip(a,a[2:])))