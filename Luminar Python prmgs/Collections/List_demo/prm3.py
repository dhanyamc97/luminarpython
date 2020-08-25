
#10
#20**2
#21**3
#22**4
#23**5
#24**6

lst=[2,4,6,7]
#------MEthod 1------
#count=1

#for i in lst:
 #   print(i**count)
  #  count+=1

#----Method 2--------

cont=len(lst)
j=1
for i in range(0,cont):
    res=lst[i]**j
    j+=1
    print(res)






