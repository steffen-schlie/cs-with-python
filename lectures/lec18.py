# Lecture 18

# Finger Exercises

# See question at:
# https://ocw.mit.edu/courses/6-100l-introduction-to-cs-and-programming-using-python-fall-2022/pages/lecture-18-more-python-class-methods/

class Circle():
    def __init__(self, radius):
        """ Initializes self with radius """
        self.r = radius

    def get_radius(self):
        """ Returns the radius of self """
        return self.r

    def __add__(self, c):
        """ c is a Circle object 
        Returns a new Circle object whose radius is 
        the sum of self and c's radius """
        return Circle(self.r + c.r)

    def __str__(self):
        """ A Circle's string representation is the radius """
        return str(self.r)


c1 = Circle(2.0)
c2 = Circle(3.0)
c = c1.__add__(c2)
print(c.get_radius())
print(c.__str__())