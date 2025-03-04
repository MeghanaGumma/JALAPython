a=list(map(int,input().split()))
v=int(input())
c=False
for i in a:
    if i==v:
        c=True
        break
print(c)
