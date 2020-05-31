n=int(input('Enter the number:'))
for i in range(n,0,-1):
    for j in range(0,i):
        print(i,end="")
        if j<=i-2:
            print('*',end='')
    print()
for i in range(1,n+1):
    for j in range(0,i):
        print(i,end="")
        if j<=i-2:
            print('*',end='')
    print()
