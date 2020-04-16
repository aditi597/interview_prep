p,q = input().split() 
n=int(p)
d=int(q)
a=list(map(int,input().split()))
c=(a[d:]+a[:d])
for i in c:
    print(i,end=" ")
