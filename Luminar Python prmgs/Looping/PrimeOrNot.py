num=int(input("Enter a Number1")) #9

flag=0

for x in range(2,num):

    for i in range(2,x):#2...8
        if(num%i==0):#9%2==0

            flag=1
            break
        else:
           flag=0

if(flag>0):
        print("Not a Prime")
else:
        print("Prime")

