# MRO=method resolution order
class Human:
    def eat(self):
        print("i can eat")
    def work(self):
        print(" i can work")
    
class Male:
    def flirt(self):
        print("i can flirt")
    
    def work(self):
        print(" i can code")
    

class Boy(Human,Male):
    def work(self):
        print("i can test")

boy_1=Boy()

boy_1.work()
print(Boy.mro()) # MRO=method resolution order
    