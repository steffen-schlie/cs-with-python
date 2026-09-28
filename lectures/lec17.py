# Lecture 17

# Finger Exercises

# See question at:
# https://ocw.mit.edu/courses/6-100l-introduction-to-cs-and-programming-using-python-fall-2022/pages/lecture-17-python-classes/

class Circle():
    def __init__(self, radius):
        """ Initializes self with radius """
        self.radius = radius

    def get_radius(self):
        """ Returns the radius of self """
        return self.radius

    def set_radius(self, radius):
        """ radius is a number
        Changes the radius of self to radius """
        self.radius = radius

    def get_area(self):
        """ Returns the area of self using pi = 3.14 """
        return self.radius*self.radius*3.14

    def equal(self, c):
        """ c is a Circle object
        Returns True if self and c have the same radius value """
        return self.radius == c.radius

    def bigger(self, c):
        """ c is a Circle object
        Returns self or c, the Circle object with the bigger radius """
        if self.radius > c.radius:
            return self
        else:
            return c
            

circ1 = Circle(4.3)
circ2 = Circle(4.2)
print(circ1.equal(circ2))
print(circ1.bigger(circ2))