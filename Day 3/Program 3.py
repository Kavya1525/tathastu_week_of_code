str =input("Enter a  string:")
s= set(str)
j=''
for i in str:
    if(i in j):
        pass
    else:
        j=j+i

print('Without duplicate string is: ',j)
