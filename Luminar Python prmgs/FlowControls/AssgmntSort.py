#sort of 3 numbers

#dob enter outpt age
num1=int(input("enter n1"))
num2=int(input("enter n2"))
num3=int(input("enter n3"))

if((num1>=num2)&(num1>num3)):
    print(num1)
    if(num2>num3):
        print(num2)
        if(num3<=num2):
            print(num3)
    else:
        print(num3)
        if(num2<=num3):
            print(num2)

elif((num2>num1)&(num2>num3)):
    print(num2)
    if (num1 > num3):
        print(num1)
        if(num3<=num1):
            print(num3)
    else:
        print(num3)
        if(num1<=num3):
            print(num1)
elif((num3>num1)&(num3>num2)):
    print(num3)
    if (num1 > num2):
        print(num1)
        if(num2<=num1):
            print(num2)
    else:
        print(num2)
        if(num1<num2):
            print(num1)
elif((num1==num2)&(num2==num3)&(num3==num1)):
    print("same")
else:
    print("2same")



