class Circle(object):
    """
    A class representing a circle with functionalities to get and set its radius, and calculate its area.
    """

    def __init__(self, radius=None):
        """
        Initializes a Circle instance with an optional radius parameter.
        """
        print("Initializing an instance")
        self._radius = radius

    @property
    def radius(self):
        """
        Gets the value of the radius.
        """
        print("Getting value: ")
        return self._radius
    
    @radius.setter
    def radius(self, radius):
        """
        Sets the value of the radius, raising a ValueError if the value is less than or equal to zero.
        """
        print(f"Setting value: {radius} ")
        if radius <= 0:
            raise ValueError("Invalid radius value: must be greater than zero")
        else:
            self._radius = radius
        
    def area(self):
        """
        Calculates the area of the circle.
        """
        return f"Area is : {3.145 * self._radius ** 2}"

a = Circle()
a.radius = 10
print(a.area())
