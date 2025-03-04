#1 what if i have a lot of init functions but ihave to call Male class init ()functions (work)
class Human:
    def __init__(self):
        self.num_eyes=2
        self.num_nose=1
        print("calling it from human")
    def eat(self):
        print("i can eat")
    def work(self):
        print(" i can work")
    
class Male:
    def __init__(self,name):
        print("calling it from male")
        self.name=name
    def flirt(self):
        print("i can flirt")
    
    def work(self):
        print(" i can code")
    

class Boy(Human,Male):
    def __init__(self,name):
        Human.__init__(self)#because here only self there is no paramters because we are not passing paramaters in human class
        Male.__init__(self,name)
    def work(self):
        print("i can test")# because here  self and parameters there are paramateers passed(name)passed in male class

boy_1=Boy("Nikhil")

print(boy_1.num_eyes)               

boy_1.work()
 
    