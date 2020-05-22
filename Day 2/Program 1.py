n=int(input("Enter the number :"))
a=2
if n%2==0:
    print(n,"is Even number")
else:
    print(n,"is Odd number")
if n>1: 
    for i in range(2,n):
        if n%i==0:
            print(n,"is not prime number")
            break
    else:
            print(n,"is a prime number")
else:
    print(n,"is not prime number")
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")    
sum = 0
temp = n
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
if n == sum:
   print("The number is an Armstrong number")
else:
   print("The number is not an Armstrong number")
