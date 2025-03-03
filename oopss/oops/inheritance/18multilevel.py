class Human:
    def __init__(self,num_heart):
        self.eyes=2
        self.heart=num_heart

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

boy_1=Boy(1)
print(boy_1.eyes)

print(boy_1.heart)
print(Boy.mro())