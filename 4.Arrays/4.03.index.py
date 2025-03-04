a=list(map(int,input().split()))
v=int(input())
idx=-1
for i in range(len(a)):
    if a[i]==v:
        idx=i
        break
print(idx)
