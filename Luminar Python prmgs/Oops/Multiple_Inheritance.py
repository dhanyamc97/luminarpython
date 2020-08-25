class Parent:
    def m1(self):
        print("Inside Parent")

class Child():
    def m2(self):
        print("Inside Child")

class SubChild(Child,Parent):
    def m3(self):
        print("Inside Subchild")

p=Parent()
p.m1()
print("\n")

c=Child()
c.m2()
print("\n")
s=SubChild()
s.m3()
s.m2()
s.m1()
