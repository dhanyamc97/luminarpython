class Sum:

    def add(self):
        num=10
        num2=20
        print(num+num2)

    def add(self,num2):
        num=20
        self.num2=30
        print(num+num2)


    def add(self,num1,num2):

        print(num1+num2)


ob=Sum()
#ob.add()
ob.add(30)
ob.add(20,30)