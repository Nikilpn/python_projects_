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
    

class Boy(Male,Human):  #first writing Male class for printimg code,method override
    pass

boy_1=Boy()
boy_1.work()

    