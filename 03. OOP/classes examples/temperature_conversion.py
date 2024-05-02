
class Temperature(object):
    """
    A class representing a temperature with functionality to convert between Celsius, Kelvin, and Fahrenheit.
    """

    def __init__(self,  celsius=None):
        """
        Initializes a Temperature instance with an optional Celsius temperature value.
        """
        self._celsius = celsius

    @property
    def celsius(self):
        """
        Gets the temperature in Celsius.
        """
        return f"{self._celsius}°C"
    
    @celsius.setter
    def celsius(self, value):
        """
        Sets the temperature in Celsius, raising a ValueError if the value is outside the valid range.
        """
        if -273.15 <= value <= 1000:
            self._celsius = value 
        else:
            raise ValueError("Invalid Celsius temperature")
        
    @property
    def kelvin(self):
        """
        Converts and gets the temperature in Kelvin.
        """
        return f"{self._celsius + 273.15}K"

    @kelvin.setter
    def kelvin(self, value):
        """
        Sets the temperature in Kelvin, raising a ValueError if the value is outside the valid range.
        """
        if 0 <= value <= 1273.15:
            self._celsius = value - 273.15
        else:
            raise ValueError("Invalid Kelvin temperature")
    
    @property
    def fahrenheit(self):
        """
        Converts and gets the temperature in Fahrenheit.
        """
        return f"{self._celsius * (9/5) + 32}°F"

    @fahrenheit.setter
    def fahrenheit(self, value):
        """
        Sets the temperature in Fahrenheit, raising a ValueError if the value is outside the valid range.
        """
        if -459.67 <= value <= 1832:
            self._celsius = (value - 32) * 5/9
        else:
            raise ValueError("Invalid Fahrenheit temperature")
        

# Testing the Temperature class
a = Temperature()
a.celsius = 0  
print(f"Celsius: {a.celsius}")
print(f"Kelvin: {a.kelvin}")
print(f"Fahrenheit: {a.fahrenheit}")
