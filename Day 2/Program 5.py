count,a=5,3
for i in range(1,4):
    count-=1
    for j in range(1,count):
        if(j==a):
            print(a)
        else:
            print(a,"*", end="")
    a-=1

for i in range(1,4):
    for j in range(1,4):
        if(j==i):
                print(i)
                break
        else:
            print(i,'*',end='')
