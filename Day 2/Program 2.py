n=int(input('How many terms: '))
x=0
y=1
print(x,end='')   
sum=0
while n-1>0:    #As we printed a number before, so we use (n-1) 
    x=y
    y=sum
    sum=x+y
    n-=1
    print(' ',sum,end='')
