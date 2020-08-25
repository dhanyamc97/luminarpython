
lst=[1,2,3,4,5,6,7,8,9,10,11,12]

elemen=int(input("Enter the element to search"))

#if elemen in lst:
#    print("Element found")
#else:
#    print("element not found")
flag=0
for i in lst:
    if(i==elemen):
        flag+=1
        break
    else:
        pass
if(flag>0):
    print("element found")
else:print("element not found")

