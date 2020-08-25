employee={
    "eid":1000,
    "ename":"person",
    "design":"tester",
    "salary":15000
}

print(employee["ename"])

#check for compny name there

print("company" in employee)

#add a new record company

employee["company"]="Luminar"
print(employee)

#update employee salary = curr + 5000

employee["salary"]+=5000
print(employee["salary"])

#print all key value pairs

for key in employee:
    print(key ,":",employee[key])