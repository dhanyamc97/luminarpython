lst=[1,2,3,4,5,6]

def even(num):
    return num%2==0


evens=list(filter(even,lst))
print(evens)

evens=list(filter(lambda n:n%2==0,lst))
print(evens)


#print all emp in caps
#print all employee sal>25000
#provide increment of 5000 for all


