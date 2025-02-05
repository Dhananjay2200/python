class shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def area(self):
        return self.x * self.y
    
class circle(shape):
    def __init__(self,radius):
        self.radius= radius
        super().__init__(radius,radius)
    def area(self):
        # return 3.14*(self.radius**2)
        return 3.14*super().area()    
sqr = shape(3,4)
print(sqr.area())

c = circle(54)
print(c.area())
