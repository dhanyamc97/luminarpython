f=open("movies.csv","r")

dict={}

for line in f:
    line=line.rstrip("\n").split(",")
    rating=line[3]

    if(rating not in dict):
        dict[rating]=1

    else:
        dict[rating]+=1

for k,v in dict.items():
    print(" rating ",k,":",v,"movies")