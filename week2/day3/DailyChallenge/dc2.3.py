#Daily Challenge - Circle
import math

class Circle:
    def __init__(self,radius):
        self.radius = radius
    def get_diameter(self):
        return self.radius*2    
# Compute the circle’s area.
    def get_area(self):
        area = math.pi * (self.radius**2)
        return area
    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter/2)
# Print the attributes of the circle — use a dunder method (__str__ or __repr__).    
    def __str__(self):
        return f'Circle radius:{self.radius}'
    def __repr__(self):
        return f'Circle({self.radius})'
# Add two circles together
#  and return a new circle with the new radius — use a dunder method (__add__).  
    def __add__(self, other):
        big_circle = Circle(self.radius + other.radius)
        return big_circle
# Compare two circles to see which is bigger — use a dunder method (__gt__).    
    def __gt__(self, other):
        return self.radius > other.radius
# Compare two circles to check if they are equal — use a dunder method (__eq__).
    def __eq__(self, other):
        return self.radius == other.radius
# Store multiple circles in a list and sort them — implement __lt__ 
# or other comparison methods.
    def __lt__(self,other):
        return self.radius < other.radius
    @staticmethod
    def sort_circles(circle_list):
        sorted_circles = sorted(circle_list)
        print("Sorted circles by radius:")
        for circle in sorted_circles:
            print(circle)



c1 = Circle(10)
c2 = Circle(8)
c3 = Circle(3)
print(c1.get_area())
print(c1.get_diameter())
c4 = Circle.from_diameter(20)
print(c4)
Circle.sort_circles([c1, c2, c3, c4])




