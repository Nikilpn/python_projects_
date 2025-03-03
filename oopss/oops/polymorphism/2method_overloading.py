#python doesnt support method overloading
# method overloading means we are defining many methods with the same name in same  class
# but it can be achieved by using *args and default argument

# class Demo:
#     def add(self,a,b):
#         return a+b
#     def add(self,a,b,c):
#         return a+b+c
# d=Demo()
# print(d.add(2,3)) #this will give you an error because python doesnt support method overloading
#


class Demo:
    def add(self,*args):
        total=0
        for i in args:
            total=total+i
        return total
d=Demo()
print(d.add(2,3,4,5,6))

