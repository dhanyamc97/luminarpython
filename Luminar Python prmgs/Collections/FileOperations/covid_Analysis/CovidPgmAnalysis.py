f=open("covid_19_india.csv","r")

dict={}
dict1={}

for lines in f:
    lines=lines.rstrip("\n").split(",")
    state=lines[3]
    death=lines[7]
    confirmed=lines[8]

    if state not in dict and  state not in dict1:
        dict[state]=death
        dict1[state]=confirmed

    else:
        dict[state] = death
        dict1[state] = confirmed

totaldeath=0
totalconfrmd=0
c_list=[]
d_list=[]

for k,v in dict.items():
    d_list.append(int(v))
    totaldeath+=int(v)
    print(k,v)

for k,v in dict.items():
    if(max(d_list)==int(v)):
        print("Maximum Death ",k,":",v)

for k, v in dict1.items():
    c_list.append(int(v))
    totalconfrmd += int(v)

for k, v in dict1.items():
    if (max(c_list) == int(v)):
        print("Maximum Confirmed ", k, ":", v)

print("Total Confirmed Case :",totalconfrmd)
print("Total Death Case :", totaldeath)






