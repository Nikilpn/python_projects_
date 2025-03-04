#acessing all parameters from init by the boy class
class Human:
    def __init__(self,num_heart):
        self.eyes=2
        self.heart=num_heart

    def eat(self):
        print(" i can eat")
    def work(self):
        print(" i can work")


class Male(Human):
    def __init__(self,name):
        print("calling from the male class")
        self.name=name
    def sleep(self):
        print("i can sleep")


class Boy(Male):

    def work(self):

        super().work()# 2.accessing two work function using super()
        print("i can code")

boy_1=Boy("Nikhil")
print(boy_1.name)



