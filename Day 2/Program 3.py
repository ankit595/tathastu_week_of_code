N=int(input("Enter size: "))
for i in range(0,N):
    for j in range(0,N):
        if (i == j) or (i+j==N-1):
            print('*', end = '')
        else:
            print(' ', end = '')
    print('')
