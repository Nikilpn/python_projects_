class Human:
    def __init__(self):
        self.num_of_eyes=2
        self.num_of_nose=1

    def eat(self):
        print("i can eat")
    def work(self):
        print(" i can work")

class Male(Human):
    def __init__(self,name):
        super().__init__()
        self.name=name

    def flirt(self):
        print("i can flirt")
    def work(self):
        super().work() #super function is for accessing upperclass methods
        
        print("i can code")

    

male_1=Male("Akash")

print(male_1.num_of_eyes)

print(male_1.name)

    