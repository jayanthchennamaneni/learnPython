class Length(object):
    __metric = {"mm" : 0.001, "cm" : 0.01, "m" : 1, "km" : 1000,
                "in" : 0.0254, "ft" : 0.3048, "yd" : 0.9144,
                "mi" : 1609.344}
    
    def __init__(self, value, unit = "m"):
        self.value = value
        self.unit = unit

    def converse2meters(self):
        return self.value * Length.__metric[self.unit]
    
    def __add__(self, other):
        return self.converse2meters() + other.converse2meters()
    
    def __str__(self):
        return str(self.converse2meters())
    
    def __repr__(self):
        return "Length(" + str(self.value) + ", '" + self.unit + "')"
    
if __name__ == "__main__":
    x = Length(4)
    y = repr(x)
    print(y)
    z = Length(4.5, "yd") + Length(1)
    z += 3
    print(z)