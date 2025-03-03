class Human:
    def eat(self):
        print("i  can eat")
    def sleep(self):
        print("i can sleep")
class Rock(Human):
    def drive(self):
        print("i Rock, can drive")
    def work(self):
        print("i am , can work")


class Male(Human):
    def beard(self):
        print("i m man, have a beard")
class Female(Human):
    def birth(self):
        print("i am female can give birth")

people1=Rock()
people1.work()
people1.eat()

people2=Female()
people2.birth()