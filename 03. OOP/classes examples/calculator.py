class Calculator(object):
    """
    A simple calculator class for basic arithmetic operations.
    """

    def __init__(self, a, b):
        """
        Initializes the calculator with two input values a and b.
        """
        self.a = a
        self.b = b
    
    def addition(self):
        """
        Performs addition of the two input values.
        """
        return self.a + self.b
    
    def subtraction(self):
        """
        Performs subtraction of the two input values.
        """
        return self.a - self.b
    
    def multiply(self):
        """
        Performs multiplication of the two input values.
        """
        return self.a * self.b
    
    def division(self):
        """
        Performs division of the two input values, avoiding division by zero.
        """
        if self.b != 0:
            return self.a / self.b
        else:
            return "Cannot divide by zero"

    def exponentiation(self):
        """
        Performs exponentiation of value a to the power of value b.
        """
        return self.a ** self.b

    def square_root_of_aandb(self):
        """
        Calculates the square root of the input values a and b, if they are non-negative.
        """
        if self.a >= 0 and self.b >= 0:
            return round(self.a ** 0.5, 2), round(self.b ** 0.5, 2)
        else:
            return "Cannot calculate square root of a negative number"

a = Calculator(2, 3)
print("Exponentiation:", a.exponentiation())
