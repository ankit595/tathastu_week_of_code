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
while(temp>0):
    dig=temp%10
    rev=rev*10+dig
    temp//=10
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")
sum = 0
temp1 = n
while temp1 > 0:
   digit = temp1 % 10
   sum += digit ** 3
   temp1 //= 10
if n == sum:
   print("The number is an Armstrong number")
else:
   print("The number is not an Armstrong number")
