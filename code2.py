class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def area(self):
        area=self.width*self.height
        return area
        
rt=Rectangle(4,6)
print(f"area is {rt.area()}")