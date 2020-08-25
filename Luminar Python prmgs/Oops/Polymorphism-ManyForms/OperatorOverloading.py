class Book:
    def __init__(self,pages):
        self.pages=pages

    def __add__(self, other):
        return Book(self.pages+other.pages)

    def __sub__(self, other):
        return (self.pages-other.pages)
    def __str__(self):

        return str(self.pages)


ob=Book(100)
ob1=Book(300)
ob2=Book(200)
print(ob+ob2)
print(ob+ob1+ob2)
