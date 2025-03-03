class Human:
    def eat(self):
        print("i can eat")
    def work(self):
        print(" i can work")

class Male(Human):
    def flirt(self):
        print("i can flirt")

    

male_1=Male()
male_1.eat()
male_1.flirt()
    