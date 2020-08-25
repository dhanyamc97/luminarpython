#dictionary

#collection name -----define

dict={}

students={"roll":100,"name":"ammu","age":25}

#keys--roll,name,age_______Values---100,ammu,25

# no dupliactes for key,,,, but for values

#print(students["name"])
#print((students["age"]))

for keys in students:
    print(keys)
    print(students[keys])

#updating value in dictionary

students["age"]+=23

print(students)

#name updation

students["name"]="Dhanya"
print(students)

#check key is availble

print("total" in students)

students["total"]=140
print(students)

