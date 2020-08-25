#funct with no argme

def factorial():
    num=int(input("Number"))
    fact=1
    for i in range(1,(num+1)):
        fact=fact*i
    print(fact)
factorial()

#fun with arg and no return
def fact(num):
     res=1
     for i in range(1,(num+1)):
         res=res*i
     return res
fact(5)






#5...>1*2*3*4