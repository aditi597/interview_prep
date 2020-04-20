# cook your dish here
for i in range(int(input())):
    s=input()
    l=len(s)
    t=(l//2)
    g=list(s[0:t])
    if(l%2==0):
        r=list(s[t:])
    else:
        r=list(s[t+1:])
    g=sorted(g)
    r=sorted(r)
    if(g==r):
        print("YES")
    else:
        print("NO")
