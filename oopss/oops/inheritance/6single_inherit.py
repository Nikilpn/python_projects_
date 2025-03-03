class Human:
    def __init__(self,num_heart):

        self.num_of_eyes=2
        self.num_of_nose=1

        self.num_heart=num_heart

    def eat(self):
        print("i can eat")
    def work(self):
        print(" i can work")

class Male(Human):
    def __init__(self,name,heart):
        super().__init__(heart)
        self.name=name

    def flirt(self):
        print("i can flirt")
    def work(self):
        super().work() #super function is for accessing upperclass methods
        
        print("i can code")

    def display(self):
        print(f"Hi iam {self.name} and i have {self.num_heart} heart")

    

male_1=Male("Akash",1)

print(male_1.num_of_eyes)

print(male_1.name)

male_1.display()

    