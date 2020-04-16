n= int(input())
l=list(map(int,input().split()))[:n]

max=l[0]
min=l[0]
for i in l:
    if i>max:
        max=i
    elif i<min:
        min=i
print(max-min)