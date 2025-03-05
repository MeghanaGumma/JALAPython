n=int(input())
temp=n
sum=0
while n!=0:
    r=n%10
    sum+=r*r*r
    n//=10
if temp==sum:
    print("Armstrong")
else:
    print("Not armstrong")
    
