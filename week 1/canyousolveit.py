
# Write your code here
t=int(input())
for i in range(t):
    n=int(input())
    a = list(map(int,input().split()))[:n]
    lis=[]
    for i in range(n):
        l=[]
        for j in range(n):
            p=((abs(a[i] - a[j]) + abs(i - j)))
            lis.append(p)
            
    print(max(lis))           
       
    
        
Language: Python 3