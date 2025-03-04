#acessing all parameters from init by the boy class
class Human:
    can_breathe=True
    print("calling it from human class")
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
    def __init__(self,heart,name,can_dance):

        Human.__init__(self,heart)
        Male.__init__(self,name)
        self.know_dancing=can_dance


    def work(self):

        super().work()# 2.accessing two work function using super()
        print("i can code")

boy_1=Boy("Nikhil",1,"True")


print(boy_1.heart)
print(boy_1.name)
print(boy_1.know_dancing)
print(boy_1.can_breathe) #it is outside declared so directly accessed


