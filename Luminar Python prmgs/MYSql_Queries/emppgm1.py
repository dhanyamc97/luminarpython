f=open("Sql_Queries")
emp={}
#fetchdata(id=1001,property="name")
for lines in f:
    id,name,design,sal=lines.rstrip("\n").split(",")
    if(id not in emp):
        emp[id]={"id":id,"name":name,"designation":design,"salary":sal}

def fetchdata(**kwargs):
    #here kwargs is dict
    #key=id
    #value=1001
    id=str(kwargs["id"])
    if(id not in emp):
        print("Employee Not Exist")
    else:
        print(emp[id]["name"])
        if "prop" in kwargs:
            val=kwargs["prop"]
            print(emp[id][val])

fetchdata(id=1001)
fetchdata(id=102)

fetchdata(id=1001,prop="salary")
fetchdata(id=1001,prop="designation")

