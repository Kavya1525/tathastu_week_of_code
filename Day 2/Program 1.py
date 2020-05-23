n= int(input("Enter the no.:"))
stt = input("Enter the string: ")
n1 = input("Enter a no. to check armstrong no.:")
if(n%2 == 0):
    print("No. is even.")
else:
    print("No. is odd. ")

count =0
for i in range(2,n):
    if(n%i == 0):
        count+=1

if(count==0):
    print("No. is prime.")
else:
    print("No. is not prime.")

rstt = stt[::-1]
if(stt == rstt):
    print("String is Palindrome.")

else:
    print("String is not Palindrome.")

arm=0
for i in n1:
    arm = arm + int(i)**3

if(arm == int(n1)):
    print("No. is armstrong")

else:
    print("No. is not armstrong")
