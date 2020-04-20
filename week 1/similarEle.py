n = int(input())
arr = list(map(int, input().strip().split()))[:n]
r = 0
for i in range(0,len(arr)):
    for j in range(0,len(arr)):
        if arr[i] == arr[j] + 1:
            r = r + 1
        elif arr[i] +1 == arr[j] and i<j:
            r = r + 1
print(r)
