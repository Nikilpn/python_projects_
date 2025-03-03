class Father:
    def sleep(self):
        print("sleeping from 10pm to 5am")
    def eat(self):
        print("eating")
class Son(Father):
    def sleep(self):
        print("sleeping from 2am to 10 am")



ram=Son() #method overriding
ram.sleep()