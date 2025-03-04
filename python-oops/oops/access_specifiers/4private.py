


class Student:
    def __init__(self,name,rollno,age):
        self.name=name #public instance variable
        self._rollno=rollno #protected instance variable
        self.__age=age
    def display(self):
        print(f" Hi iam {self.name} and my roll no is {self._rollno}, and from student class and iam {self.__age} years old")
class Branch(Student):
    pass


s1=Student("Nisha",22,10)
s1.name="Nikhil"

# print(s1.__age) #not possible it is private,even from derived class,but using name mangling we can access private

s1.display()
