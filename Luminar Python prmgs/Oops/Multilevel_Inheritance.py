class Parent:
    def m1(self):
        print("Inside Parent")

class Child(Parent):
    def m2(self):
        print("Inside Child")

class SubChild(Child):
    def m3(self):
        print("Inside Subchild")

ch=Child()
ch.m1()
ch.m2()

sc=SubChild()
sc.m3()
sc.m2()
sc.m1()





