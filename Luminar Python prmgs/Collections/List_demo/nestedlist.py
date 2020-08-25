employees=[[1001,'ammu',15000],
           [1002,"achu",20000],
           [1003,"aami",18000],
           [1004,"aju",13000]]

for emp in employees:
    if(emp[2]>17000):
        print(emp[1])
sum=0
for emp in employees:
    sum+=emp[2]
print(sum)

