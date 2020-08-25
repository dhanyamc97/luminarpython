lst=[1,2,3,4,5]

lst.sort()
element=int(input(" Enter the Element"))

low=0
upp=len(lst)-1

while(low<=upp):
    data=lst[low]+lst[upp]

    if(data==element):
        print("pairs ",lst[low],",",lst[upp])
        break
    elif(data>element):
        upp=upp-1
    else:
        low=low+1