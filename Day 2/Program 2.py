n = int(input("Enter the no. upto fibonacci series : "))
a,b=0,1
count=0
sum=0

if(n<=0):
    print("Incorrect No.")
elif(n==1):
    print(a)

else:
    print("Fibonacci series:")
    while(count<n):
        print(a, end=' ')
        sum = a + b
            # update values
        a = b
        b = sum
        count = count + 1
