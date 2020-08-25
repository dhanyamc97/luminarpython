low=int(input("enter the low "))
uppr=int(input("enter the upper "))

even_sum=0
odd_sum=0

for i in range(low,uppr):
    if(i%2==0):
        even_sum+=i
    else:
        odd_sum+=i
print(even_sum)
print(odd_sum)