


class Student:
    def __init__(self,name,rollno):
        self.name=name #public instance variable
        self._rollno=rollno #protected instance variable
    def display(self):
        print(f" Hi iam {self.name} and my roll no is {self._rollno}, and from student class")
class Branch(Student):
    pass


b1=Branch("Nisha",22)


b1.display() #we are not directly aceesing the roll no (eg-b1._rollno)
            #we are acessing with the help of display function