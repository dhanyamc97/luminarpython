# Check Palindrome or not

num=int(input("Enter a number:"))
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if(temp==rev):
    print("The number is palindrome!")
else:
    print("Not a palindrome!")


a=input("Enter a number")
b=a[::-1]
if(a==b):
    print("Palindrome")
else:
    print("Not a Palindrome")