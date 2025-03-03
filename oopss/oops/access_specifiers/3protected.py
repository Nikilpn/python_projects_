


class Student:
    def __init__(self,name,rollno):
        self.name=name #public instance variable
        self._rollno=rollno #protected instance variable
    def display(self):
        print(f" Hi iam {self.name} and my roll no is {self._rollno}, and from student class")
class Branch(Student):
    pass


s1=Student("Nisha",22)
s1.name="Nikhil"
s1._rollno=100 #better not to use like this..its our responsibilty not to use outside

s1.display() #we are not directly aceesing the roll no (eg-b1._rollno)
            #we are acessing with the help of display function