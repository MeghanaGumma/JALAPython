a=list(map(int,input().split()))
s=0
for i in a:
    s+=i
avg=s/len(a) if a else 0
print(avg)
