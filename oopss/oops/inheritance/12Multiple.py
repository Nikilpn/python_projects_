
class Human:
    def __init__(self,num_heart):
        self.num_eyes=2
        self.num_nose=1
        self.num_heart=1
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
    def __init__(self,name,heart,language):
        Human.__init__(self,heart)
        Male.__init__(self,name)
        self.language=language
    def work(self):
        print("i can test")# because here  self and parameters there are paramateers passed(name)passed in male class
    def display(self):
        print(f"hi iam {self.name},i have {self.num_heart}heart and i have {self.num_eyes} eyes and i work in {self.language}")
boy_1=Boy("Nikhil",1,"python")

print(boy_1.num_nose)
print(boy_1.num_heart)
print(boy_1.language)
boy_1.display()
boy_1.work()
 
    