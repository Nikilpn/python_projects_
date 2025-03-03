class Human:
    def eat(self):
        print("i can eat")
    
class Male:
    def flirt(self):
        print("i can flirt")

class Boy(Human,Male):
    pass

boy_1=Boy()
boy_1.eat()
boy_1.flirt()

    