# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    q=list(map(int,input().split()))[:n]
    z=0
    a=q[::-1]
    for i in q:
        if((i>7 or i<1)):
            z=1
    if(a==q and z!=1):
        print("yes")
    else:
        print("no")
