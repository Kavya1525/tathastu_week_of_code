for i in range(5,0,-1):
    for j in range(i,0,-1):
        print('*',end=' ')

    for j in range(2*(5-i)):
        print(" ",end=" ")

    for j in range(i, 0, -1):
        print('*', end=' ')

    print()
for i in range(1,6):
    for j in range(i):
        print('*',end=' ')

    for j in range(2 * (5 - i)):
        print(" ", end=" ")

    for j in range(i):
        print('*',end=' ')

    print()
