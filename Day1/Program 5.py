a =int(input(" enter the score of 1 player in 60 balls "))
b= int(input("enter a score of 2 player in 60 ball"))
c = int(input("enter a score of 3 player in 60 ball"))       
s1 = (a/60)*100
s2 = (b/60)*100
s3 = (c/60)*100

print("strike rate of 1st 2nd and 3rd player are :", s1,s2,s3,sep='\n')
print("id=f they played 60 more balls then score will be ......")
a = 2*a
b = 2*b
c = 2*c
print("scores oof 1st 2nd and 3rd player are :",a,b,c,sep='\n')
print("maximum no. of sixes hit by each player :",a //6,b // 6, c//6, sep='\n')
