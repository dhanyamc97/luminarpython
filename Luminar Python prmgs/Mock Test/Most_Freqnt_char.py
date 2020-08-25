st="ABABABCAAA"

dict={}

for char in st:

  if(char not in dict):
      dict[char]=1

  else:
      dict[char]+=1

d_list =[]

for k,v in dict.items():
    d_list.append(int(v))

for k,v in dict.items():
    if(max(d_list)==int(v)):
        print(" frequent ",k,":",v)