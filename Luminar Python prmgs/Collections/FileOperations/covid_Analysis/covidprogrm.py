f=open("covid_19_india.csv","r")


dict={}
dict1={}

for lines in f:
    data=lines.rstrip("\n").split(",")
    state=data[3]
    case = data[8]
    death=data[7]

    if(state not in dict):
        dict[state]=case
    else:
       old=dict[state]

       if(case>old):
           dict[state]=case

    if (state not in dict1):
        dict1[state] = death
    else:
        old = dict1[state]

        if (death > old):
            dict1[state] = death

print("***********state", ",", "cases*************")
for k,v in dict.items():  # map each state with death count
     print(k,v)


print("***********state", ",", "death*************")
for k,v in dict1.items():  # map each state with death count
     print(k,v)







#     print("Highest value of death",death)

# print(word)






#and print which has hghest value




#print which has highest confirmed case




#calculate total number of confimed case in india




# calculate total number of death in india