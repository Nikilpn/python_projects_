class Human:
    def eat(self):
        print(" i can eat")
class Male(Human):
    def sleep(self):
        print("i can sleep")
        
class Boy(Male):
    pass
boy_1=Boy()
boy_1.eat()
boy_1.sleep()