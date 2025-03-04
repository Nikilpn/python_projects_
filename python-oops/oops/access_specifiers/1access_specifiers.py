


class Student:
    def __init__(self,name):
        self.name=name #public instance variable

    def display(self):
        print(f" Hi iam {self.name} and from student class")
class Branch:
    pass
s1=Student("Nikhil")
print(s1.name)
s1.display()
