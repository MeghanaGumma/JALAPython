n=int(input())
i=1
c=0
while i<=n:
    if n%i==0:
        c=c+1
    i=i+1
if c==2:
    print('It is a prime number')
else:
    print('It is not a prime number')
