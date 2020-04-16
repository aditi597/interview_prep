n,q = list(map(int,input().split()))
lst = list(map(int,input().split()))
for _ in range(q):
    temp = list(map(int,input().split()))
    if len(temp) == 2:
        if lst[temp[1]-1] == 0:
            lst[temp[1]-1] = 1
        else:
            lst[temp[1]-1] = 0
    else:
        if lst[temp[2]-1] == 1:
            print("ODD")
        else:
            print("EVEN")
