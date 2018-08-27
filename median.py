n=int(input(""))
a=[int(x) for x in input().split()]
a.sort()
k=int((n+1)/2)
print(a[k-1],end='')
