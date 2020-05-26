lst = [i for i in input("Enter the list items:").split()]
j=[]
for i in lst:
    if(i not in j):
        j.append(i)

print('Without duplicate list is: ',j)
