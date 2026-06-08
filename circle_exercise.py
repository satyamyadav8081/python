class circle:
    pi=3.14 #class object attribute
    def __init__(self,radius=6):
        self.radius=radius
    def get_circumferrences(self):
        return 2 * self.pi * self.radius
circle=circle(4)
print(circle.get_circumferrences())    