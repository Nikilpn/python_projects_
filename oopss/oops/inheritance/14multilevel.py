# accessing two work function

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
        Human.work(self) # accessing two work function
        print("i can code")



boy_1 = Boy()
boy_1.work()