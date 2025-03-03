class Circle:
    pi=3.14
    def __init__(self,radius):
        self.radius=radius

    
    def Circumference(self):
        circum=2*self.pi*self.radius
        return circum
    

    def area(self):
        area=self.pi*self.radius**2
        return area

circle_1=Circle(3)
print(circle_1.Circumference())

print(circle_1.area())


