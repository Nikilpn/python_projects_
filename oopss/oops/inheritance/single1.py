class Person:
    def setvalue1(self,*args):
        self.name=args[0]
        self.age=args[1]
        self.place=args[2]

class Employee(Person):

    def setvalue2(self,phone,job):
        self.phone=phone
        self.job=job
    
    def printvalue(self):
        print(self.name)
        print(self.job)
        print(self.phone)
        print(self.place)
employee1=Employee()
employee1.setvalue1("vinay",32,"thrissur")
employee1.setvalue2(1234567890,"software engineer")

employee1.printvalue()