line="hello hai hello hai"

words=line.split(" ")
lst=[]

dict={}

for word in words:
    if(word not in dict):
        dict[word]=1
    else:
        dict[word]+=1

print(dict)


