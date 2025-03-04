class Human:
    def __init__(self):
        print("init from human class")
        self.eyes=2

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

boy_1=Boy()
print(boy_1.eyes)