t=int(input())
for i in range(t):
    s=list(input())
    l=[]
    for i in s:
        if i not in l:
            l.append(i)
    for i in l:
        print(i,end="")
    print()
    