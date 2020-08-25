f=open("temperature","r")

dict={}
data=[]


for lines in f:

    data=lines.rstrip("\n").split(",")
    district=data[0]
    tempter=data[1]


    if(district not in dict):
        dict[district]=tempter
    else:
        old=dict[district]
        if(tempter>old):
            dict[district]=tempter
print(dict)




