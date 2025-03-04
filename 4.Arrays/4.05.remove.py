a=list(map(int,input().split()))
v=int(input())
a_new=[]
for i in a:
    if i!=v:
        a_new.append(i)
print(a_new)
