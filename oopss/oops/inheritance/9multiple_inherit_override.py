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
    pass
   

boy_1=Boy()

Male.work(boy_1) #solution1 for printing i can code (Boy)inherited from male class 

    