lst=[10,11,12,13,14,15,2,3,4]

lst.sort()
print(lst)

low=0
upp=len(lst)-1
element=int(input(" Enter the number to search"))
flag=0

while(low<=upp):
 mid=(low+upp)//2

 if(element>lst[mid]):
        low=mid+1
 elif(element<lst[mid]):
        upp=mid-1
 elif(element==lst[mid]):
        flag+=1
        break

if(flag>0):
    print("Element Found")
else:
    print("Element not found")

