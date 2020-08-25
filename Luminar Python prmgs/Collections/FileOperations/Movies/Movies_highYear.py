f=open("movies.csv","r")

dict={}
ls=[]

for line in f:
    line=line.rstrip("\n").split(",")
    year=line[2]

    if(year not in dict):
        dict[year]=1
    else:
        dict[year]+=1

for k,v in dict.items():
    ls.append(int(v))

for k,v in dict.items():
    if(max(ls)==int(v)):
        print("Maximum no. of movies in",k,"-",v)

