class Employee:

    def setEmployee(self,eid,ename,desgn,salary):
        self.eid=eid
        self.ename=ename
        self.desgn=desgn
        self.salary=salary

    def printValues(self):
        print(self.eid)
        print(self.ename)
        print(self.desgn)
        print(self.salary)

emp=Employee()
emp.setEmployee(100,"Ammu","Trainee",28000)
emp.printValues()
