f=open("movies.csv","r")

dict={}
lst=[]

for lines in f:
    lines=lines.rstrip().split(",")
    year=lines[2]

    if(year not in dict):
        dict[year]=1
    else:
        dict[year]+=1

for k,v in dict.items():
    print("year ",k ,"-",v,"Movies")
