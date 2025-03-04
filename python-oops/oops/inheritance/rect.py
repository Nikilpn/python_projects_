class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area_of_rect(self):
        areaa=self.length*self.breadth
        return areaa
    
rectangle1=Rectangle(3,3)
print(rectangle1.area_of_rect())