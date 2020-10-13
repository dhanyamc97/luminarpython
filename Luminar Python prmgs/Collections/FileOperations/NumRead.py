
f=open("number","r")

lst=[]
even=[]
odd=[]

for num in f:

    lst.append(int(num.rstrip("\n")))
res=sum(lst)
print(res)

for n_num in lst:
    if(n_num%2==0):
        even.append(n_num)
    else:
        odd.append(n_num)
print(even)
print(odd)

a=10
b=20

a,b = b,a
print(a,b)





# rstrip to remove \n


