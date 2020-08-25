class Employee:

    def __init__(self,eid,ename,desgn,salary):
        self.eid=eid
        self.ename=ename
        self.desgn=desgn
        self.salary=salary

    def printValues(self):
        print(self.eid)
        print(self.ename)
        print(self.desgn)
        print(self.salary)

    def __str__(self):
        return  self.ename


emp=Employee(1,"ammu","studnt",23000)
emp1=Employee(2,"achu","studnt",25000)
emp2=Employee(1,"addu","studnt",33000)

lst=[]

lst.append(emp)
lst.append(emp2)
lst.append(emp1)

for em in lst:
    max_sal=max(em.salary)
    if(em.salary==max_sal):
        print(em)




