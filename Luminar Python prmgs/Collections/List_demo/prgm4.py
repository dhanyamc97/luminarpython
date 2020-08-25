lst=[1,2,3,4]

#6 = 2,4
#7 = 3,4

elemnt=int(input("enter num"))
n=len(lst)
flag=0
for i in range(0,n):
    for j in range(0,n):
        if((i+j)==elemnt):
            flag>=1
            break
        else:
           pass
if(flag>=1):
      print(i,j)
else:
      print(" n")



  # asssgnmnt-2
 #[2,4,6]=[10,8,6]
 #[3,5,8]=[13,11,8]
