


class Student:
    def __init__(self,name,rollno,age):
        self.name=name #public instance variable
        self._rollno=rollno #protected instance variable
        self.__age=age
    def __display(self):
        print(f" Hi iam {self.name} and my roll no is {self._rollno}, and from student class and iam {self.__age} years old")
class Branch(Student):
    pass


s1=Student("Nisha",22,10)
s1.name="Nikhil"

print(dir(s1))#name mangling
print(s1._Student__age)# by student mangling we are aceesing private

s1._Student__display()



