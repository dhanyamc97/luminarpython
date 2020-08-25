num1=int(input("enter n1"))
num2=int(input("enter n2"))
num3=int(input("enter n3"))

if((num1>num2)&(num1>num3)):
    print("Max= num1",num1)
    if(num2>num3):
        print("num2 is second largest",num2)
    else:
        print("Num3 is second largst",num3)
elif((num2>num1)&(num2>num3)):
    print("Max= num2",num2)
    if (num1 > num3):
        print("num1 is second largest",num1)
    else:
        print("Num3 is second largst",num3)
elif((num3>num1)&(num3>num2)):
    print("Max =",num3)
    if (num1 > num2):
        print("num1 is second largest",num1)
    else:
        print("Num3 is second largst",num2)
else:
    print("same")
