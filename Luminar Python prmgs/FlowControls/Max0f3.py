
num1=int(input("Enter number1"))
num2=int(input("Enter number2"))
num3=int(input("Enter number3"))

if((num1>num2)&(num1>num3)):
    print("Max= num1",num1)
elif((num2>num1)&(num2>num3)):
    print("Max= num2",num2)
elif((num3>num1)&(num3>num2)):
    print("Max =",num3)
else:
    print("same")

