for i in range(1,9):
    for j in range(1,9):
        if(j==i):
            print('*',end='')
        elif(i==9-j):
            print('*',end='')
        else:
            print(' ', end='')
    print()
