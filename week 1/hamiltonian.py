
# Write your code here
n=int(input())
a = list(map(int,input().split()))[:n]
for i in range(n-1):
    l=[]
    for j in range(i+1,n):
        l.append(a[j])
        
        m=max(l)
    if a[i]>m:
        print(a[i],end=" ")
print(a[n-1],end=" ")
   
