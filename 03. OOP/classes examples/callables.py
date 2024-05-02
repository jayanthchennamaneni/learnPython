class Playing(object):
    def __init__(self, *games):
        self.games = games
    
    # Call method to concatenate the available games
    def __call__(self):
        result = ", ".join(self.games) + " are available"
        return result
    
a = Playing("tabletennis", "football", "cricket", "badminton")
print(a())  
b = Playing("geogusser", "fishing")
print(b()) 



class Triangle(object):
    # Call method to calculate the area of the triangle
    def __call__(self, a, b, c):
        z = (a + b + c) / 2
        area = (z * (z - a) * (z - b) * (z - c)) ** 0.5
        return area

r = Triangle()
print(r(3, 4, 6))


class StraightLines():
    def __init__(self, m, c):
        self.slope = m
        self.y_intercept = c
        
    def __call__(self, x):
        return self.slope * x + self.y_intercept
    
line = StraightLines(0.4, 3)
for x in range(-5, 6):
    print(x, line(x))









# 70 (tiskunnam) - 7.90 (migilnavi) => 62.10
# 62.10 - 10(ne frnd tiskunavi) => 52.10 (manam spend chesam)
# 52.10/2 => 26.05 (naku/niku)
# 26.05 + 10  => 36.05 (niku)





