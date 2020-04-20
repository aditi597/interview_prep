c=0
for i in range(t):
    n=int(input())
    a = list(map(int,input().split()))[:n]
    for i in a:
        if i!=0:
            print(i,end=" ")
            c+=1
    for i in range(n-c):
        print(0,end=" ")
