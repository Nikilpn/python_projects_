class Human:
    def eat(self):
        print("i can eat")
    def work(self):
        print(" i can work")

class Male(Human):
    def flirt(self):
        print("i can flirt")
    def work(self):
        super().work() #super function is for accessing upperclass methods
        
        print("i can code")

    

male_1=Male()

male_1.eat()



male_1.work()
    