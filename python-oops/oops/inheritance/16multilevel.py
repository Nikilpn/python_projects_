

class Human:
    def eat(self):
        print(" i can eat")
    def work(self):
        print(" i can work")


class Male(Human):
    def sleep(self):
        print("i can sleep")


class Boy(Male):
    def work(self):

        super().work()# 2.accessing two work function using super()
        print("i can code")
class Programme(Boy):
    def work(self):
        Boy.work(self)
        print("i can programme")




programmer_1=Programme()
programmer_1.work()
print('*'*100)
