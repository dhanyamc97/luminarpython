low_limit=int(input("Enter the Lower Limit"))
limit=int(input("Enter Limit"))


while(low_limit<=limit):
    if(low_limit%2==0):
        print(low_limit)
    low_limit+=1
